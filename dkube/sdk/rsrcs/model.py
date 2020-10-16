from __future__ import print_function
import time
import sys

from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.rest import ApiException

from dkube.sdk.internal.dkube_api.models.datum_model import DatumModel
from dkube.sdk.internal.dkube_api.models.git_access_info import GitAccessInfo
from dkube.sdk.internal.dkube_api.models.git_access_credentials import GitAccessCredentials
from dkube.sdk.internal.dkube_api.models.s3_access_credentials import S3AccessCredentials
from dkube.sdk.internal.dkube_api.models.gcs_access_info import GCSAccessInfo
from dkube.sdk.internal.dkube_api.models.repo_gcs_access_info_secret import RepoGCSAccessInfoSecret
from dkube.sdk.internal.dkube_api.models.nfs_access_info import NFSAccessInfo
from dkube.sdk.internal.dkube_api.models.redshift_access_info import RedshiftAccessInfo
from dkube.sdk.internal.dkube_api.models.datum_model_k8svolume import DatumModelK8svolume

from pprint import pprint

from .util import *


class DkubeModel(object):
    DATASET_SOURCES = ["dvs", "git", "aws_s3", "s3", "gcs", "nfs", "k8svolume"]
    GIT_ACCESS_OPTS = ["apikey", "sshkey", "password"]

    def __init__(self, user, name=generate("dataset"), tags=None):
        self.k8svolume = DatumModelK8svolume(name=None)

        self.nfsaccess = NFSAccessInfo(server=None, path=None)

        self.gcssecret = RepoGCSAccessInfoSecret(name=None, content=None)
        self.gcsaccess = GCSAccessInfo(
            bucket=None, prefix=None, secret=self.gcssecret)

        self.s3access = S3AccessCredentials(
            access_key_id=None, access_key=None, bucket=None, prefix=None, endpoint=None)

        self.gitcreds = GitAccessCredentials(
            username=None, password=None, apikey=None, sshkey=None, private=True)
        self.gitaccess = GitAccessInfo(
            path=None, url=None, branch=None, credentials=self.gitcreds)

        self.datum = DatumModel(name=None, tags=None, _class='model',
                                dvs=None, source='dvs', url=None, remote=False, gitaccess=self.gitaccess,
                                s3access=self.s3access, nfsaccess=self.nfsaccess, gcsaccess=self.gcsaccess)

        self.update_basic(user, name, tags)

    def update_basic(self, user, name, tags):
        tags = list_of_strs(tags)

        self.user = user
        self.name = name

        self.datum.name = name
        self.datum.tags = tags

    def update_model_source(self, source=DATASET_SOURCES[0]):
        self.datum.source = source

    def update_git_details(self, url, branch=None, authopt=GIT_ACCESS_OPTS[0], authval=None):
        self.datum.source = "git"
        self.datum.url = url
        self.gitaccess.url = url
        self.gitaccess.branch = branch

        self.gitcreds.username = self.user

        if authmode == 'apikey':
            self.gitcreds.apikey = authval
        elif authmode == 'password':
            self.gitcreds.password = authval
        elif authmode == 'sshkey':
            self.gitcreds.sshkey = authval

    def update_awss3_details(self, bucket, prefix, key, secret):

        self.datum.source = "aws_s3"
        self.s3access.bucket = bucket
        self.s3access.prefix = prefix
        self.s3access.access_key_id = key
        self.s3access.access_key = secret

    def update_s3_details(self, endpoint, bucket, prefix, key, secret):

        self.datum.source = "s3"
        self.s3access.endpoint = endpoint
        self.s3access.prefix = prefix
        self.s3access.bucket = bucket
        self.s3access.access_key_id = key
        self.s3access.access_key = secret

    def update_gcs_details(self, bucket, prefix, key, secret):

        self.datum.source = "gcs"
        self.gcsaccess.bucket = bucket
        self.gcsaccess.prefix = prefix
        self.gcssecret.name = key
        self.gcssecret.content = secret

    def update_nfs_details(self, server, path="/"):

        self.datum.source = "nfs"
        self.nfsaccess.path = path
        self.nfsaccess.server = server

    def update_k8svolume_details(self, name):

        self.datum.source = "k8svolume"
        self.k8svolume.name = name
