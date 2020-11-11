"""

.. module:: DKubeAPI
   :synopsis: Helper class which provides high level methods for user to integrate at workflow level.

.. moduleauthor:: Ahmed Khan <github.com/mak-454>


"""

import json
import os
import time

import pandas as pd
import pyarrow as pa
from dkube.sdk.internal.api_base import *
from dkube.sdk.rsrcs import *


class DkubeApi(ApiBase):

    """

        This class encapsules all the high level dkube workflow functions.::

            from dkube.sdk import *
            dapi = DkubeApi()

        *Inputs*

            URL
                FQDN endpoint at which DKube platform is deployed::

                    http://dkube-controller-master.dkube.cluster.local:5000

                    https://dkube.ai:32222

                .. note:: If not provided then the value is picked from *DKUBE_ACCESS_URL* env variable. If not found then http://dkube-controller-master.dkube.cluster.local:5000 is used assuming the access is internal to the DKube cluster


            token
                Access token for the APIs, without which DKube will return 40x codes

                .. note:: If not provided then the value is picked from *DKUBE_ACCESS_TOKEN* env variable. ASSERTs if env is not defined.


            common_tags
                Tags which need to applied all the resources created using this API object


            req_timeout
                Timeout for all the requests which are issued using this API object


            req_retries
                Number of retries per request

    """

    def __init__(self, URL=None, token=None, common_tags=[], req_timeout=None, req_retries=None):

        self.url = URL
        if self.url == None:
            self.url = os.getenv(
                "DKUBE_ACCESS_URL", "http://dkube-controller-master.dkube.cluster.local:5000")

        self.token = token
        if self.token == None:
            self.token = os.getenv("DKUBE_ACCESS_TOKEN", None)
            assert self.token == None, "TOKEN must be specified either by passing argument or by setting DKUBE_ACCESS_TOKEN env variable"

        self.common_tags = common_tags
        super().__init__(self.url, self.token)

    def validate_token(self):
        """
            Method which can be used to validate the token. 
            Returns the JWT Claims. Which contains the role assigned to the user.


        """

        return super().validate_token()

    def create_training_run(self, run: DkubeTraining, wait_for_completion=True):
        """
            Method to create a training run on DKube.
            Raises Exception in case of errors.


            *Inputs*

                run
                    Instance of :bash:`dkube.sdk.rsrcs.Training` class.
                    Please see the :bash:`Resources` section for details on this class.


                wait_for_completion
                    When set to :bash:`True` this method will wait for job to complete after submission.
                    Job is declared complete if it is one of the :bash:`complete/failed/error` state

        """

        assert type(
            run) == DkubeTraining, "Invalid type for run, value must be instance of rsrcs:DkubeTraining class"
        super().create_run(run)
        while wait_for_completion:
            status = super().get_run('training', run.user, run.name, fields='status')
            state, reason = status['state'], status['reason']
            if state.lower() in ['complete', 'failed', 'error']:
                print(
                    "run {} - completed with state {} and reason {}".format(run.name, state, reason))
                break
            else:
                print(
                    "run {} - waiting for completion, current state {}".format(run.name, state))
                time.sleep(10)

    def get_training_run(self, user, name):
        """
            Method to fetch the training run with given name for the given user.
            Raises exception in case of run is not found or any other connection errors.

            *Inputs*

                user
                    User whose training run has to be fetched.
                    In case of if token is of different user, then the token should have permission to fetch the
                    training run of the :bash:`user` in the input. They should be in same DKube group.

                name
                    Name of the training run to be fetched

        """

        return super().get_run('training', user, name)

    def list_training_runs(self, user, filters='*'):
        """
            Method to list all the training runs of a user.
            Raises exception on any connection errors.

            *Inputs*

                user
                    User whose training runs must be fetched.
                    In case of if token is of different user, then the token should have permission to fetch the
                    training runs of the :bash:`user` in the input. They should be in same DKube group.

                filters
                    Only :bash:`*` is supported now.

                    User will able to filter runs based on state or duration

        """

        return super().list_runs('training', user)

    def delete_training_run(self, user, name):
        """
            Method to delete a run.
            Raises exception if token is of different user or if training run with name doesnt exist or on any connection errors.

            *Inputs*

                user
                    The token must belong to this user. As run of different user cannot be deleted.

                name
                    Name of the run which needs to be deleted.

        """

        super().delete_run('training', user, name)

    def create_preprocessing_run(self, run: DkubePreprocessing, wait_for_completion=True):
        """
            Method to create a preprocessing run on DKube.
            Raises Exception in case of errors.


            *Inputs*

                run
                    Instance of :bash:`dkube.sdk.rsrcs.Preprocessing` class.
                    Please see the :bash:`Resources` section for details on this class.


                wait_for_completion
                    When set to :bash:`True` this method will wait for job to complete after submission.
                    Job is declared complete if it is one of the :bash:`complete/failed/error` state

        """

        assert type(
            run) == DkubePreprocessing, "Invalid type for run, value must be instance of rsrcs:DkubePreprocessing class"
        super().create_run(run)
        while wait_for_completion:
            status = super().get_run('preprocessing', run.user, run.name, fields='status')
            state, reason = status['state'], status['reason']
            if state.lower() in ['complete', 'failed', 'error']:
                print(
                    "run {} - completed with state {} and reason {}".format(run.name, state, reason))
                break
            else:
                print(
                    "run {} - waiting for completion, current state {}".format(run.name, state))
                time.sleep(10)

    def get_preprocessing_run(self, user, name):
        """
            Method to fetch the preprocessing run with given name for the given user.
            Raises exception in case of run is not found or any other connection errors.

            *Inputs*

                user
                    User whose preprocessing run has to be fetched.
                    In case of if token is of different user, then the token should have permission to fetch the
                    preprocessing run of the :bash:`user` in the input. They should be in same DKube group.

                name
                    Name of the training run to be fetched

        """

        return super().get_run('preprocessing', user, name)

    def list_preprocessing_runs(self, user, filters='*'):
        """
            Method to list all the preprocessing runs of a user.
            Raises exception on any connection errors.

            *Inputs*

                user
                    User whose preprocessing runs must be fetched.
                    In case of if token is of different user, then the token should have permission to fetch the
                    preprocessing runs of the :bash:`user` in the input. They should be in same DKube group.

                filters
                    Only :bash:`*` is supported now.

                    User will able to filter runs based on state or duration

        """

        return super().list_runs('preprocessing', user)

    def delete_preprocessing_run(self, user, name):
        """
            Method to delete a run.
            Raises exception if token is of different user or if preprocessing run with name doesnt exist or on any connection errors.

            *Inputs*

                user
                    The token must belong to this user. As run of different user cannot be deleted.

                name
                    Name of the run which needs to be deleted.

        """

        super().delete_run('preprocessing', user, name)

    def create_test_inference(self, run: DkubeServing, wait_for_completion=True):
        """
            Method to create a test inference on DKube.
            Raises Exception in case of errors.


            *Inputs*

                run
                    Instance of :bash:`dkube.sdk.rsrcs.serving` class.
                    Please see the :bash:`Resources` section for details on this class.


                wait_for_completion
                    When set to :bash:`True` this method will wait for job to complete after submission.
                    Job is declared complete if it is one of the :bash:`complete/failed/error` state

        """

        assert type(
            run) == DkubeServing, "Invalid type for run, value must be instance of rsrcs:DkubeServing class"
        super().create_run(run)
        while wait_for_completion:
            status = super().get_run('inference', run.user, run.name, fields='status')
            state, reason = status['state'], status['reason']
            if state.lower() in ['complete', 'failed', 'error', 'running']:
                print(
                    "run {} - completed with state {} and reason {}".format(run.name, state, reason))
                break
            else:
                print(
                    "run {} - waiting for completion, current state {}".format(run.name, state))
                time.sleep(10)

    def get_test_inference(self, user, name):
        """
            Method to fetch the test inference with given name for the given user.
            Raises exception in case of run is not found or any other connection errors.

            *Inputs*

                user
                    User whose test inference has to be fetched.
                    In case of if token is of different user, then the token should have permission to fetch the
                    serving run of the :bash:`user` in the input. They should be in same DKube group.

                name
                    Name of the serving run to be fetched

        """

        return super().get_run('inference', user, name)

    def list_test_inferences(self, user, filters='*'):
        """
            Method to list all the training inferences of a user.
            Raises exception on any connection errors.

            *Inputs*

                user
                    User whose test inferences must be fetched.
                    In case of if token is of different user, then the token should have permission to fetch the
                    serving runs of the :bash:`user` in the input. They should be in same DKube group.

                filters
                    Only :bash:`*` is supported now.

                    User will able to filter runs based on state or duration

        """

        return super().list_runs('inference', user)

    def delete_test_inference(self, user, name):
        """
            Method to delete a test inference.
            Raises exception if token is of different user or if serving run with name doesnt exist or on any connection errors.

            *Inputs*

                user
                    The token must belong to this user. As run of different user cannot be deleted.

                name
                    Name of the run which needs to be deleted.

        """

        super().delete_run('inference', user, name)

    def create_project(self, project: DkubeProject, wait_for_completion=True):
        """
            Method to create a project on DKube.
            Raises Exception in case of errors.


            *Inputs*

                project
                    Instance of :bash:`dkube.sdk.rsrcs.project` class.
                    Please see the :bash:`Resources` section for details on this class.


                wait_for_completion
                    When set to :bash:`True` this method will wait for project resource to get into one of the complete state.
                    Project is declared complete if it is one of the :bash:`complete/failed/error` state

        """

        assert type(
            project) == DkubeProject, "Invalid type for run, value must be instance of rsrcs:DkubeProject class"
        super().create_repo(project)
        while wait_for_completion:
            status = super().get_repo('program', project.user, project.name, fields='status')
            state, reason = status['state'], status['reason']
            if state.lower() in ['ready', 'failed', 'error']:
                print(
                    "project {} - completed with state {} and reason {}".format(project.name, state, reason))
                break
            else:
                print(
                    "project {} - waiting for completion, current state {}".format(project.name, state))
                time.sleep(10)

    def get_project(self, user, name):
        """
            Method to fetch the project with given name for the given user.
            Raises exception in case of project is not found or any other connection errors.

            *Inputs*

                user
                    User whose project has to be fetched.
                    In case of if token is of different user, then the token should have permission to fetch the
                    project of the :bash:`user` in the input. They should be in same DKube group.

                name
                    Name of the project to be fetched

        """

        return super().get_repo('program', user, name)

    def list_projects(self, user, filters='*'):
        """
            Method to list all the projects of a user.
            Raises exception on any connection errors.

            *Inputs*

                user
                    User whose projects must be fetched.
                    In case of if token is of different user, then the token should have permission to fetch the
                    projects of the :bash:`user` in the input. They should be in same DKube group.

                filters
                    Only :bash:`*` is supported now.

                    User will able to filter projects based on state or the source

        """

        return super().list_repos('program', user)

    def delete_project(self, user, name):
        """
            Method to delete a project.
            Raises exception if token is of different user or if project with name doesnt exist or on any connection errors.

            *Inputs*

                user
                    The token must belong to this user. As project of different user cannot be deleted.

                name
                    Name of the project which needs to be deleted.

        """

        super().delete_repo('program', user, name)

################### Feature Store ############################
    def create_featureset(self, featureset: DkubeFeatureSet, data):
        assert type(
            featureset) == DkubeFeatureSet, "Invalid type for run, value must be instance of rsrcs:DkubeFeatureset class"
        response = super().create_featureset(data, featureset.user, featureset.name)
        return response

    def delete_featureset(self, featureset, wait_for_completion=True):
        return super().delete_featureset(featureset)

    def read_featureset(self, featureset, path=None, filename='featureset.parquet'):
        df_empty = pd.DataFrame({'A': []})
        if path is None and self.CONFIG_FILE is None:
            return {"data": df_empty, "status": -1, "error": "Path of featureset not found"}
        if path is None:
            with open(self.CONFIG_FILE) as json_file:
                fsconfig = json.load(json_file)
            featuresets = fsconfig["inputs"]["featuresets"]
            for each_feature in featuresets:
                if each_feature["name"] == featureset:
                    path = each_feature["location"]
        if path is None:
            return {"data": df_empty, "status": -1, "error": "Featureset doesn't exist"}
        try:
            table = pq.read_table(os.path.join(path, filename))
            feature_df = table.to_pandas()
            return {"data": feature_df, "status": 0, "error": None}
        except Exception as e:
            return {"data": df_empty, "status": -1, "error": e}

    def write_featureset(self, dataframe, featureset, path=None, filename='featureset.parquet'):
        if path is None and self.CONFIG_FILE is None:
            return {"status": -1, "error": "Path of featureset not found"}
        if path is None:
            with open(self.CONFIG_FILE) as json_file:
                fsconfig = json.load(json_file)
            featuresets = fsconfig["outputs"]["featuresets"]
            for each_feature in featuresets:
                if each_feature["name"] == featureset:
                    path = each_feature["location"]
        if path is None:
            return {"status": -1, "error": "Featureset doesn't exist"}
        try:
            table = pa.Table.from_pandas(dataframe)
            pq.write_table(table, os.path.join(path, filename))
            return {"status": 0, "error": None}
        except Exception as e:
            return {"status": -1, "error": e}

    def commit_featureset(self, featuresset, path):
        if path is None and self.CONFIG_FILE is None:
            return {"error": "Path of featureset not found"}
        if path is None:
            with open(self.CONFIG_FILE) as json_file:
                fsconfig = json.load(json_file)
            featuresets = fsconfig["outputs"]["featuresets"]
            for each_feature in featuresets:
                if each_feature["name"] == featureset:
                    path = each_feature["location"]
        if path is None:
            return {"status": -1, "error": "Featureset doesn't exist"}
        return super().commit_feature_version(featureset, path)

    def list_featureset(self):
        return super().list_featureset()

###############################################################

    def create_dataset(self, dataset: DkubeDataset, wait_for_completion=True):
        """
            Method to create a dataset on DKube.
            Raises Exception in case of errors.


            *Inputs*

                dataset
                    Instance of :bash:`dkube.sdk.rsrcs.dataset` class.
                    Please see the :bash:`Resources` section for details on this class.


                wait_for_completion
                    When set to :bash:`True` this method will wait for dataset resource to get into one of the complete state.
                    dataset is declared complete if it is one of the :bash:`complete/failed/error` state

        """

        assert type(
            dataset) == DkubeDataset, "Invalid type for run, value must be instance of rsrcs:DkubeDataset class"
        super().create_repo(dataset)
        while wait_for_completion:
            status = super().get_repo('dataset', dataset.user, dataset.name, fields='status')
            state, reason = status['state'], status['reason']
            if state.lower() in ['ready', 'failed', 'error']:
                print(
                    "dataset {} - completed with state {} and reason {}".format(dataset.name, state, reason))
                break
            else:
                print(
                    "dataset {} - waiting for completion, current state {}".format(dataset.name, state))
                time.sleep(10)

    def get_dataset(self, user, name):
        """
            Method to fetch the dataset with given name for the given user.
            Raises exception in case of dataset is not found or any other connection errors.

            *Inputs*

                user
                    User whose dataset has to be fetched.
                    In case of if token is of different user, then the token should have permission to fetch the
                    dataset of the :bash:`user` in the input. They should be in same DKube group.

                name
                    Name of the dataset to be fetched

        """

        return super().get_repo('dataset', user, name)

    def list_datasets(self, user, filters='*'):
        """
            Method to list all the datasets of a user.
            Raises exception on any connection errors.

            *Inputs*

                user
                    User whose datasets must be fetched.
                    In case of if token is of different user, then the token should have permission to fetch the
                    datasets of the :bash:`user` in the input. They should be in same DKube group.

                filters
                    Only :bash:`*` is supported now.

                    User will able to filter datasets based on state or the source

        """

        return super().list_repos('dataset', user)

    def delete_dataset(self, user, name):
        """
            Method to delete a dataset.
            Raises exception if token is of different user or if dataset with name doesnt exist or on any connection errors.

            *Inputs*

                user
                    The token must belong to this user. As dataset of different user cannot be deleted.

                name
                    Name of the dataset which needs to be deleted.

        """

        super().delete_repo('dataset', user, name)

    def create_model(self, model: DkubeModel, wait_for_completion=True):
        """
            Method to create a model on DKube.
            Raises Exception in case of errors.


            *Inputs*

                model
                    Instance of :bash:`dkube.sdk.rsrcs.model` class.
                    Please see the :bash:`Resources` section for details on this class.


                wait_for_completion
                    When set to :bash:`True` this method will wait for model resource to get into one of the complete state.
                    model is declared complete if it is one of the :bash:`complete/failed/error` state

        """

        assert type(
            model) == DkubeModel, "Invalid type for run, value must be instance of rsrcs:DkubeModel class"
        super().create_repo(model)
        while wait_for_completion:
            status = super().get_repo('model', model.user, model.name, fields='status')
            state, reason = status['state'], status['reason']
            if state.lower() in ['ready', 'failed', 'error']:
                print(
                    "model {} - completed with state {} and reason {}".format(model.name, state, reason))
                break
            else:
                print(
                    "model {} - waiting for completion, current state {}".format(model.name, state))
                time.sleep(10)

    def get_model(self, user, name):
        """
            Method to fetch the model with given name for the given user.
            Raises exception in case of model is not found or any other connection errors.

            *Inputs*

                user
                    User whose model has to be fetched.
                    In case of if token is of different user, then the token should have permission to fetch the
                    model of the :bash:`user` in the input. They should be in same DKube group.

                name
                    Name of the model to be fetched

        """

        return super().get_repo('model', user, name)

    def list_models(self, user, filters='*'):
        """
            Method to list all the models of a user.
            Raises exception on any connection errors.

            *Inputs*

                user
                    User whose models must be fetched.
                    In case of if token is of different user, then the token should have permission to fetch the
                    models of the :bash:`user` in the input. They should be in same DKube group.

                filters
                    Only :bash:`*` is supported now.

                    User will able to filter models based on state or the source

        """

        return super().list_repos('model', user)

    def delete_model(self, user, name):
        """
            Method to delete a model.
            Raises exception if token is of different user or if model with name doesnt exist or on any connection errors.

            *Inputs*

                user
                    The token must belong to this user. As model of different user cannot be deleted.

                name
                    Name of the model which needs to be deleted.

        """

        super().delete_repo('model', user, name)

    def trigger_runs_byproject(self, project, user):
        """
            Method to trigger all the runs in dkube which uses the mentioned project.

            *Inputs*

                project
                    Name of the project.

                user
                    Owner of the project. All runs of this user will be retriggered.

        """

        condition = TriggerCondition(match='project', name=project, user=user)
        return super().trigger_runs(condition)

    def trigger_runs_bydataset(self, dataset, user):
        """
            Method to trigger all the runs in dkube which uses the mentioned dataset in input.

            *Inputs*

                dataset
                    Name of the dataset.

                user
                    Owner of the dataset. All runs of this user will be retriggered.

        """
        condition = TriggerCondition(match='dataset', name=dataset, user=user)
        return super().trigger_runs(condition)

    def trigger_runs_bymodel(self, model, user):
        """
            Method to trigger all the runs in dkube which uses the mentioned model in input.

            *Inputs*

                model
                    Name of the model.

                user
                    Owner of the model. All runs of this user will be retriggered.

        """

        condition = TriggerCondition(match='model', name=model, user=user)
        return super().trigger_runs(condition)
