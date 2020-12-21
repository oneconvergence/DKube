from __future__ import print_function
from pprint import pprint

import sys
import time

from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.models.git_access_credentials import GitAccessCredentials
from dkube.sdk.internal.dkube_api.models.git_access_info import GitAccessInfo
from dkube.sdk.internal.dkube_api.models.datum_model import DatumModel
from dkube.sdk.internal.dkube_api.rest import ApiException

from .util import *


class DkubeProject(object):

    """

        This class defines the DKube project with helper functions to set properties of project.::

            from dkube.sdk import *
            mnist = DkubeProject("oneconv", name="mnist")

            Where first argument is the user of this project. User should be a valid onboarded user in dkube.

    """

    GIT_ACCESS_OPTS = ["apikey", "sshkey", "password"]

    """
    List of authentication options supported for git data source.

    :bash:`apikey` :- Github APIKey based authentication. This must have permission on the repo to clone and checkout.

    :bash:`sshkey` :- Git SSH key based authentication.

    :bash:`password` :- Standard username/password based. 

	"""

    def __init__(self, user, name=generate("project"), tags=None):
        self.gitcreds = GitAccessCredentials(
            username=None, password=None, apikey=None, sshkey=None, private=True)
        self.gitaccess = GitAccessInfo(
            path=None, url=None, branch=None, credentials=self.gitcreds)
        self.datum = DatumModel(name=None, tags=None, _class='program',
                                dvs=None, source='git', url=None, remote=False, gitaccess=self.gitaccess)

        self.update_basic(user, name, tags)

    def update_basic(self, user, name, tags):
        tags = list_of_strs(tags)

        self.user = user
        self.name = name

        self.datum.name = name
        self.datum.tags = tags

    def update_git_details(self, url, branch=None, authopt=GIT_ACCESS_OPTS[0], authval=None):

        """
            Method to update the details of git datasource.

            *Inputs*

                url
                    A valid Git URL. Following are considered as valid URLs.

                    - CloneURL : https://github.com/oneconvergence/dkube.git

                    - TreeURL : https://github.com/oneconvergence/dkube/tree/2.1.dev/dkube

                    - BlobURL : https://github.com/oneconvergence/dkube/blob/2.1.dev/dkube/sdk/api.py

                    - ZipURL : https://github.com/oneconvergence/dkube/archive/2.1.dev.zip

                branch
                    Valid branch of git repo. If not provided then **master** branch is used by default.

                authopt
                    One of the valid option from **GIT_ACCESS_OPTS**

                authval
                    Value corresponding to the authopt
        """

        self.datum.url = url
        self.gitaccess.url = url
        self.gitaccess.branch = branch

        self.gitcreds.username = self.user

        if authopt == 'apikey':
            self.gitcreds.apikey = authval
        elif authopt == 'password':
            self.gitcreds.password = authval
        elif authopt == 'sshkey':
            self.gitcreds.sshkey = authval