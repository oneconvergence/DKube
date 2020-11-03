"""Dkube Launcher for kubeflow pipelines

Usage:
    dkube.py [--name=NAME] [--token=TOKEN] [--command=COMMAND] [--training=TRAINING] [--preprocessing=PREPROCESSING] [--serving=SERVING] [--custom=CUSTOM] [--runid=RUNID] [--workflowid=WORKFLOWID]
    dkube.py (-h | --help)
    dkube.py --version

Options:
    -h --help                           Show this screen.
    --version                           Show version.
    --name=NAME                         User specified name of the pipeline stage
    --token=TOKEN                       Authentication token of logged in user
    --command=COMMAND                   Command to execute. project/dataset/model/training/preprocessing/serving/custom.
    --training=TRAINING                 Training job definition. JSON str of dkube.sdk.rsrcs:DkubeTraining
    --preprocessing=PREPROCESSING       Preprocessing job definition. JSON str of dkube.sdk.rsrcs:DkubePreprocessing
    --serving=SERVING                   Serving job definition. JSON str of dkube.sdk.rsrcs:DkubeServing
    --custom=CUSTOM                     Custom job definition. JSON str of dkube.sdk.rsrcs.DkubeCustom 
    --runid=RUNID                       Unique ID of the pipeline run for back reference.
    --workflowid=WORKFLOWID             Unique ID of the pipeline workflow for back reference.
"""

from .docopt import docopt
from pyfiglet import Figlet

import os
import json
import time

from dkube.sdk import *

from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.rest import ApiException

from url_normalize import url_normalize

# Configure API key authorization: d3apikey
configuration = dkube_api.Configuration()
configuration.api_key_prefix['Authorization'] = 'Bearer'

#Bug: Go via proxy since token-info API is not returning claims on direct http call
#dkubeURL = 'http://dkube-controller-master.dkube:5000'
dkubeURL  = 'https://dkube-proxy.dkube'
configuration.host = url_normalize('{}/dkube/v2/controller'.format(dkubeURL))
configuration.verify_ssl = False


def run_outputs(user, _class, name):
    api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
    gresponse = api.jobs_get_collection_one(user, _class, name)

    job = gresponse.to_dict()['data']['job']
    uuid = job['parameters']['generated']['uuid'] 

    with open("/tmp/rundetails", "w+") as op:
        op.write(json.dumps(job))

    lresponse = api.get_one_run_lineage(user, _class, uuid)
    outputs = lresponse.to_dict()['data']['outputs']

    artifacts = [
                    {'datum': output['version']['datum_name'], 'class': output['version']['datum_type'],
                     'version': output['version']['uuid'], 'index': output['version']['index']
                    }
                    for output in outputs
                ]

    with open("/tmp/artifacts", "w+") as op:
        op.write(json.dumps(artifacts))

def command_serving(name='', user='', serving='', runid='', workflowid='', **kwargs):
    stagename = name

    runname = generate('plserving')

    run = json.loads(serving)
    run['name'] = runname
    run['parameters']['class'] = 'inference'
    #run['parameters']['inference']['tags'].extend(['owner=pipeline', 'stage='+name, 'workflowid='+workflowid, 'runid='+runid])

    api = DkubeApi(URL=dkubeURL, token=kwargs['token'])
    inf = run['parameters']['inference']
    if inf['serving_image']['image'] == None or (
            inf['transformer'] == True and inf['transformer_image']['image'] == None) or (
                inf['transformer'] == True and inf['transformer_project'] == None):

        if inf['version'] == None:
            v = api.get_model_latest_version(inf['owner'], inf['model'])
            inf['version'] = v['uuid']

        li = api.get_model_lineage(inf['owner'], inf['model'], inf['version'])
        if inf['serving_image']['image'] == None:
            si = li['run']['parameters']['generated']['serving_image']['image']
            inf['serving_image']['image'] = dict(si)

        if inf['transformer'] == True and inf['transformer_image']['image'] == None:
            ti = li['run']['parameters']['generated']['training_image']['image']
            inf['transformer_image']['image'] = dict(ti)

        if inf['transformer'] == True and inf['transformer_project'] == None:
            code = li['run']['parameters']['training']['datums']['workspace']['data']
            inf['transformer_project'] = code['name']
            inf['transformer_commit_id'] = code['version']

    run['parameters']['inference'] = inf
    api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
    api.jobs_add_one(user, run, run='true')
    while True:
        response = api.jobs_get_collection_one(user, 'inference', runname)
        status = response.to_dict()['data']['job']['parameters']['generated']['status']
        state, reason = status['state'], status['reason']
        if state.lower() in ['running', 'failed', 'error']:
            print("run {} - completed with state {} and reason {}".format(runname, state, reason))
            break
        else:
            print("run {} - waiting for completion, current state {}".format(runname, state))
            time.sleep(10)

    #generate the outputs, next stage can pick from here
    run_outputs(user, 'inference', runname)


def command_preprocessing(name='', user='', preprocessing='', runid='', workflowid='', **kwargs):
    stagename=name

    runname = generate('pldata')

    run = json.loads(preprocessing)
    run['name'] = runname
    run['parameters']['class'] = 'preprocessing'
    run['parameters']['preprocessing']['tags'].extend(['owner=pipeline', 'stage='+stagename, 'workflowid='+workflowid, 'runid='+runid])

    api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
    api.jobs_add_one(user, run, run='true')
    while True:
        response = api.jobs_get_collection_one(user, 'preprocessing', runname)
        status = response.to_dict()['data']['job']['parameters']['generated']['status']
        state, reason = status['state'], status['reason']
        if state.lower() in ['complete', 'failed', 'error']:
            print("run {} - completed with state {} and reason {}".format(runname, state, reason))
            break
        else:
            print("run {} - waiting for completion, current state {}".format(runname, state))
            time.sleep(10)

    #generate the outputs, next stage can pick from here
    run_outputs(user, 'preprocessing', runname)

def command_training(name='', user='', training='', runid='', workflowid='',**kwargs):
    stagename = name

    runname = generate('pltraining')

    run = json.loads(training)
    run['name'] = runname
    run['parameters']['class'] = 'training'
    run['parameters']['training']['tags'].extend(['owner=pipeline', 'stage='+stagename, 'workflowid='+workflowid, 'runid='+runid])

    api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
    api.jobs_add_one(user, run, run='true')
    while True:
        response = api.jobs_get_collection_one(user, 'training', runname)
        status = response.to_dict()['data']['job']['parameters']['generated']['status']
        state, reason = status['state'], status['reason']
        if state.lower() in ['complete', 'failed', 'error']:
            print("run {} - completed with state {} and reason {}".format(runname, state, reason))
            break
        else:
            print("run {} - waiting for completion, current state {}".format(runname, state))
            time.sleep(10)

    #generate the outputs, next stage can pick from here
    run_outputs(user, 'training', runname)

def validate_token(token):
    configuration.api_key['Authorization'] = token

    api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))

    response = api.tokeninfo()
    claims = response.to_dict()['data']
    user = claims['username']
    role = claims['role']

    return user, role

def main():
    args = docopt(__doc__, version='1.4')
    data = {}
    for key, val in args.items():
        data[key.lstrip('--')] = val

    command = data['command']

    f = Figlet(font='slant')
    print(f.renderText('Dkube {}'.format(command.capitalize())))

    user, role = validate_token(data['token'])
    data.update({'user': user, 'role': role, 'token': data['token']})
    fn = 'command_{}'.format(command)
    globals()[fn](**data)
