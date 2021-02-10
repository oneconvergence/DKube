# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.2.1.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DatumModelGenerated(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'deleted': 'bool',
        'archived': 'bool',
        'extract': 'bool',
        'original_name': 'str',
        'private': 'str',
        'head_version_index': 'int',
        'head_version': 'str',
        'updated_time': 'TimeStamps',
        'storage_path': 'str',
        'affinity': 'str',
        'uuid': 'str',
        'status': 'DatumStatusModel',
        'refresh_status': 'DatumStatusModel',
        'size': 'str',
        'progress': 'int',
        'timestamps': 'TimeStamps',
        'tbref': 'str',
        'user': 'str',
        'details': 'DatumModelGeneratedDetails'
    }

    attribute_map = {
        'deleted': 'deleted',
        'archived': 'archived',
        'extract': 'extract',
        'original_name': 'originalName',
        'private': 'private',
        'head_version_index': 'head_version_index',
        'head_version': 'head_version',
        'updated_time': 'updated_time',
        'storage_path': 'storage_path',
        'affinity': 'affinity',
        'uuid': 'uuid',
        'status': 'status',
        'refresh_status': 'refresh_status',
        'size': 'size',
        'progress': 'progress',
        'timestamps': 'timestamps',
        'tbref': 'tbref',
        'user': 'user',
        'details': 'details'
    }

    def __init__(self, deleted=False, archived=False, extract=None, original_name=None, private=None, head_version_index=None, head_version=None, updated_time=None, storage_path=None, affinity=None, uuid=None, status=None, refresh_status=None, size=None, progress=None, timestamps=None, tbref=None, user=None, details=None):  # noqa: E501
        """DatumModelGenerated - a model defined in Swagger"""  # noqa: E501
        self._deleted = None
        self._archived = None
        self._extract = None
        self._original_name = None
        self._private = None
        self._head_version_index = None
        self._head_version = None
        self._updated_time = None
        self._storage_path = None
        self._affinity = None
        self._uuid = None
        self._status = None
        self._refresh_status = None
        self._size = None
        self._progress = None
        self._timestamps = None
        self._tbref = None
        self._user = None
        self._details = None
        self.discriminator = None
        if deleted is not None:
            self.deleted = deleted
        if archived is not None:
            self.archived = archived
        if extract is not None:
            self.extract = extract
        if original_name is not None:
            self.original_name = original_name
        if private is not None:
            self.private = private
        if head_version_index is not None:
            self.head_version_index = head_version_index
        if head_version is not None:
            self.head_version = head_version
        if updated_time is not None:
            self.updated_time = updated_time
        if storage_path is not None:
            self.storage_path = storage_path
        if affinity is not None:
            self.affinity = affinity
        if uuid is not None:
            self.uuid = uuid
        if status is not None:
            self.status = status
        if refresh_status is not None:
            self.refresh_status = refresh_status
        if size is not None:
            self.size = size
        if progress is not None:
            self.progress = progress
        if timestamps is not None:
            self.timestamps = timestamps
        if tbref is not None:
            self.tbref = tbref
        if user is not None:
            self.user = user
        if details is not None:
            self.details = details

    @property
    def deleted(self):
        """Gets the deleted of this DatumModelGenerated.  # noqa: E501


        :return: The deleted of this DatumModelGenerated.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this DatumModelGenerated.


        :param deleted: The deleted of this DatumModelGenerated.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def archived(self):
        """Gets the archived of this DatumModelGenerated.  # noqa: E501


        :return: The archived of this DatumModelGenerated.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this DatumModelGenerated.


        :param archived: The archived of this DatumModelGenerated.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def extract(self):
        """Gets the extract of this DatumModelGenerated.  # noqa: E501


        :return: The extract of this DatumModelGenerated.  # noqa: E501
        :rtype: bool
        """
        return self._extract

    @extract.setter
    def extract(self, extract):
        """Sets the extract of this DatumModelGenerated.


        :param extract: The extract of this DatumModelGenerated.  # noqa: E501
        :type: bool
        """

        self._extract = extract

    @property
    def original_name(self):
        """Gets the original_name of this DatumModelGenerated.  # noqa: E501


        :return: The original_name of this DatumModelGenerated.  # noqa: E501
        :rtype: str
        """
        return self._original_name

    @original_name.setter
    def original_name(self, original_name):
        """Sets the original_name of this DatumModelGenerated.


        :param original_name: The original_name of this DatumModelGenerated.  # noqa: E501
        :type: str
        """

        self._original_name = original_name

    @property
    def private(self):
        """Gets the private of this DatumModelGenerated.  # noqa: E501


        :return: The private of this DatumModelGenerated.  # noqa: E501
        :rtype: str
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this DatumModelGenerated.


        :param private: The private of this DatumModelGenerated.  # noqa: E501
        :type: str
        """

        self._private = private

    @property
    def head_version_index(self):
        """Gets the head_version_index of this DatumModelGenerated.  # noqa: E501


        :return: The head_version_index of this DatumModelGenerated.  # noqa: E501
        :rtype: int
        """
        return self._head_version_index

    @head_version_index.setter
    def head_version_index(self, head_version_index):
        """Sets the head_version_index of this DatumModelGenerated.


        :param head_version_index: The head_version_index of this DatumModelGenerated.  # noqa: E501
        :type: int
        """

        self._head_version_index = head_version_index

    @property
    def head_version(self):
        """Gets the head_version of this DatumModelGenerated.  # noqa: E501


        :return: The head_version of this DatumModelGenerated.  # noqa: E501
        :rtype: str
        """
        return self._head_version

    @head_version.setter
    def head_version(self, head_version):
        """Sets the head_version of this DatumModelGenerated.


        :param head_version: The head_version of this DatumModelGenerated.  # noqa: E501
        :type: str
        """

        self._head_version = head_version

    @property
    def updated_time(self):
        """Gets the updated_time of this DatumModelGenerated.  # noqa: E501


        :return: The updated_time of this DatumModelGenerated.  # noqa: E501
        :rtype: TimeStamps
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this DatumModelGenerated.


        :param updated_time: The updated_time of this DatumModelGenerated.  # noqa: E501
        :type: TimeStamps
        """

        self._updated_time = updated_time

    @property
    def storage_path(self):
        """Gets the storage_path of this DatumModelGenerated.  # noqa: E501

        Local path of datum stored in dkube storage  # noqa: E501

        :return: The storage_path of this DatumModelGenerated.  # noqa: E501
        :rtype: str
        """
        return self._storage_path

    @storage_path.setter
    def storage_path(self, storage_path):
        """Sets the storage_path of this DatumModelGenerated.

        Local path of datum stored in dkube storage  # noqa: E501

        :param storage_path: The storage_path of this DatumModelGenerated.  # noqa: E501
        :type: str
        """

        self._storage_path = storage_path

    @property
    def affinity(self):
        """Gets the affinity of this DatumModelGenerated.  # noqa: E501

        Affinity of this datum.  # noqa: E501

        :return: The affinity of this DatumModelGenerated.  # noqa: E501
        :rtype: str
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """Sets the affinity of this DatumModelGenerated.

        Affinity of this datum.  # noqa: E501

        :param affinity: The affinity of this DatumModelGenerated.  # noqa: E501
        :type: str
        """

        self._affinity = affinity

    @property
    def uuid(self):
        """Gets the uuid of this DatumModelGenerated.  # noqa: E501


        :return: The uuid of this DatumModelGenerated.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DatumModelGenerated.


        :param uuid: The uuid of this DatumModelGenerated.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def status(self):
        """Gets the status of this DatumModelGenerated.  # noqa: E501


        :return: The status of this DatumModelGenerated.  # noqa: E501
        :rtype: DatumStatusModel
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DatumModelGenerated.


        :param status: The status of this DatumModelGenerated.  # noqa: E501
        :type: DatumStatusModel
        """

        self._status = status

    @property
    def refresh_status(self):
        """Gets the refresh_status of this DatumModelGenerated.  # noqa: E501


        :return: The refresh_status of this DatumModelGenerated.  # noqa: E501
        :rtype: DatumStatusModel
        """
        return self._refresh_status

    @refresh_status.setter
    def refresh_status(self, refresh_status):
        """Sets the refresh_status of this DatumModelGenerated.


        :param refresh_status: The refresh_status of this DatumModelGenerated.  # noqa: E501
        :type: DatumStatusModel
        """

        self._refresh_status = refresh_status

    @property
    def size(self):
        """Gets the size of this DatumModelGenerated.  # noqa: E501

        Size in bytes  # noqa: E501

        :return: The size of this DatumModelGenerated.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DatumModelGenerated.

        Size in bytes  # noqa: E501

        :param size: The size of this DatumModelGenerated.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def progress(self):
        """Gets the progress of this DatumModelGenerated.  # noqa: E501

        Progress in percentage  # noqa: E501

        :return: The progress of this DatumModelGenerated.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this DatumModelGenerated.

        Progress in percentage  # noqa: E501

        :param progress: The progress of this DatumModelGenerated.  # noqa: E501
        :type: int
        """

        self._progress = progress

    @property
    def timestamps(self):
        """Gets the timestamps of this DatumModelGenerated.  # noqa: E501


        :return: The timestamps of this DatumModelGenerated.  # noqa: E501
        :rtype: TimeStamps
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        """Sets the timestamps of this DatumModelGenerated.


        :param timestamps: The timestamps of this DatumModelGenerated.  # noqa: E501
        :type: TimeStamps
        """

        self._timestamps = timestamps

    @property
    def tbref(self):
        """Gets the tbref of this DatumModelGenerated.  # noqa: E501


        :return: The tbref of this DatumModelGenerated.  # noqa: E501
        :rtype: str
        """
        return self._tbref

    @tbref.setter
    def tbref(self, tbref):
        """Sets the tbref of this DatumModelGenerated.


        :param tbref: The tbref of this DatumModelGenerated.  # noqa: E501
        :type: str
        """

        self._tbref = tbref

    @property
    def user(self):
        """Gets the user of this DatumModelGenerated.  # noqa: E501

        user to which this datum belongs  # noqa: E501

        :return: The user of this DatumModelGenerated.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DatumModelGenerated.

        user to which this datum belongs  # noqa: E501

        :param user: The user of this DatumModelGenerated.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def details(self):
        """Gets the details of this DatumModelGenerated.  # noqa: E501


        :return: The details of this DatumModelGenerated.  # noqa: E501
        :rtype: DatumModelGeneratedDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this DatumModelGenerated.


        :param details: The details of this DatumModelGenerated.  # noqa: E501
        :type: DatumModelGeneratedDetails
        """

        self._details = details

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DatumModelGenerated, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DatumModelGenerated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
