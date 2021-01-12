# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FeatureSetDef(object):
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
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'owner': 'str',
        'created_ts': 'str',
        'updated_ts': 'str',
        'job': 'str',
        'status': 'str',
        'uuid': 'str',
        'deleted': 'bool',
        'archived': 'bool',
        'original_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'owner': 'owner',
        'created_ts': 'created_ts',
        'updated_ts': 'updated_ts',
        'job': 'job',
        'status': 'status',
        'uuid': 'uuid',
        'deleted': 'deleted',
        'archived': 'archived',
        'original_name': 'originalName'
    }

    def __init__(self, name=None, description=None, tags=None, owner=None, created_ts=None, updated_ts=None, job=None, status=None, uuid=None, deleted=False, archived=False, original_name=None):  # noqa: E501
        """FeatureSetDef - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._tags = None
        self._owner = None
        self._created_ts = None
        self._updated_ts = None
        self._job = None
        self._status = None
        self._uuid = None
        self._deleted = None
        self._archived = None
        self._original_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if owner is not None:
            self.owner = owner
        if created_ts is not None:
            self.created_ts = created_ts
        if updated_ts is not None:
            self.updated_ts = updated_ts
        if job is not None:
            self.job = job
        if status is not None:
            self.status = status
        if uuid is not None:
            self.uuid = uuid
        if deleted is not None:
            self.deleted = deleted
        if archived is not None:
            self.archived = archived
        if original_name is not None:
            self.original_name = original_name

    @property
    def name(self):
        """Gets the name of this FeatureSetDef.  # noqa: E501


        :return: The name of this FeatureSetDef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeatureSetDef.


        :param name: The name of this FeatureSetDef.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this FeatureSetDef.  # noqa: E501


        :return: The description of this FeatureSetDef.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FeatureSetDef.


        :param description: The description of this FeatureSetDef.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this FeatureSetDef.  # noqa: E501

        User specified custom tags  # noqa: E501

        :return: The tags of this FeatureSetDef.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FeatureSetDef.

        User specified custom tags  # noqa: E501

        :param tags: The tags of this FeatureSetDef.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def owner(self):
        """Gets the owner of this FeatureSetDef.  # noqa: E501


        :return: The owner of this FeatureSetDef.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this FeatureSetDef.


        :param owner: The owner of this FeatureSetDef.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def created_ts(self):
        """Gets the created_ts of this FeatureSetDef.  # noqa: E501


        :return: The created_ts of this FeatureSetDef.  # noqa: E501
        :rtype: str
        """
        return self._created_ts

    @created_ts.setter
    def created_ts(self, created_ts):
        """Sets the created_ts of this FeatureSetDef.


        :param created_ts: The created_ts of this FeatureSetDef.  # noqa: E501
        :type: str
        """

        self._created_ts = created_ts

    @property
    def updated_ts(self):
        """Gets the updated_ts of this FeatureSetDef.  # noqa: E501


        :return: The updated_ts of this FeatureSetDef.  # noqa: E501
        :rtype: str
        """
        return self._updated_ts

    @updated_ts.setter
    def updated_ts(self, updated_ts):
        """Sets the updated_ts of this FeatureSetDef.


        :param updated_ts: The updated_ts of this FeatureSetDef.  # noqa: E501
        :type: str
        """

        self._updated_ts = updated_ts

    @property
    def job(self):
        """Gets the job of this FeatureSetDef.  # noqa: E501


        :return: The job of this FeatureSetDef.  # noqa: E501
        :rtype: str
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this FeatureSetDef.


        :param job: The job of this FeatureSetDef.  # noqa: E501
        :type: str
        """

        self._job = job

    @property
    def status(self):
        """Gets the status of this FeatureSetDef.  # noqa: E501


        :return: The status of this FeatureSetDef.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FeatureSetDef.


        :param status: The status of this FeatureSetDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["Created", "Ready", "Updating", "Deleting", "Error"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def uuid(self):
        """Gets the uuid of this FeatureSetDef.  # noqa: E501

        Unique id generated by system (timestamp in milliseconds)  # noqa: E501

        :return: The uuid of this FeatureSetDef.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this FeatureSetDef.

        Unique id generated by system (timestamp in milliseconds)  # noqa: E501

        :param uuid: The uuid of this FeatureSetDef.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def deleted(self):
        """Gets the deleted of this FeatureSetDef.  # noqa: E501


        :return: The deleted of this FeatureSetDef.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this FeatureSetDef.


        :param deleted: The deleted of this FeatureSetDef.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def archived(self):
        """Gets the archived of this FeatureSetDef.  # noqa: E501


        :return: The archived of this FeatureSetDef.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this FeatureSetDef.


        :param archived: The archived of this FeatureSetDef.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def original_name(self):
        """Gets the original_name of this FeatureSetDef.  # noqa: E501


        :return: The original_name of this FeatureSetDef.  # noqa: E501
        :rtype: str
        """
        return self._original_name

    @original_name.setter
    def original_name(self, original_name):
        """Sets the original_name of this FeatureSetDef.


        :param original_name: The original_name of this FeatureSetDef.  # noqa: E501
        :type: str
        """

        self._original_name = original_name

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
        if issubclass(FeatureSetDef, dict):
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
        if not isinstance(other, FeatureSetDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
