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


class ArtifactVolume(object):
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
        'artifact_type': 'str',
        'artifact_name': 'str',
        'artifact_version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'artifact_type': 'artifact_type',
        'artifact_name': 'artifact_name',
        'artifact_version': 'artifact_version'
    }

    def __init__(self, name=None, artifact_type=None, artifact_name=None, artifact_version=None):  # noqa: E501
        """ArtifactVolume - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._artifact_type = None
        self._artifact_name = None
        self._artifact_version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if artifact_type is not None:
            self.artifact_type = artifact_type
        if artifact_name is not None:
            self.artifact_name = artifact_name
        if artifact_version is not None:
            self.artifact_version = artifact_version

    @property
    def name(self):
        """Gets the name of this ArtifactVolume.  # noqa: E501


        :return: The name of this ArtifactVolume.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArtifactVolume.


        :param name: The name of this ArtifactVolume.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def artifact_type(self):
        """Gets the artifact_type of this ArtifactVolume.  # noqa: E501


        :return: The artifact_type of this ArtifactVolume.  # noqa: E501
        :rtype: str
        """
        return self._artifact_type

    @artifact_type.setter
    def artifact_type(self, artifact_type):
        """Sets the artifact_type of this ArtifactVolume.


        :param artifact_type: The artifact_type of this ArtifactVolume.  # noqa: E501
        :type: str
        """
        allowed_values = ["dataset", "program", "model", "featureset"]  # noqa: E501
        if artifact_type not in allowed_values:
            raise ValueError(
                "Invalid value for `artifact_type` ({0}), must be one of {1}"  # noqa: E501
                .format(artifact_type, allowed_values)
            )

        self._artifact_type = artifact_type

    @property
    def artifact_name(self):
        """Gets the artifact_name of this ArtifactVolume.  # noqa: E501


        :return: The artifact_name of this ArtifactVolume.  # noqa: E501
        :rtype: str
        """
        return self._artifact_name

    @artifact_name.setter
    def artifact_name(self, artifact_name):
        """Sets the artifact_name of this ArtifactVolume.


        :param artifact_name: The artifact_name of this ArtifactVolume.  # noqa: E501
        :type: str
        """

        self._artifact_name = artifact_name

    @property
    def artifact_version(self):
        """Gets the artifact_version of this ArtifactVolume.  # noqa: E501


        :return: The artifact_version of this ArtifactVolume.  # noqa: E501
        :rtype: str
        """
        return self._artifact_version

    @artifact_version.setter
    def artifact_version(self, artifact_version):
        """Sets the artifact_version of this ArtifactVolume.


        :param artifact_version: The artifact_version of this ArtifactVolume.  # noqa: E501
        :type: str
        """

        self._artifact_version = artifact_version

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
        if issubclass(ArtifactVolume, dict):
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
        if not isinstance(other, ArtifactVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
