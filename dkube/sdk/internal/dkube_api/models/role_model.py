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

class RoleModel(object):
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
        'capabilities': 'list[CapabilitiesModel]'
    }

    attribute_map = {
        'name': 'name',
        'capabilities': 'capabilities'
    }

    def __init__(self, name=None, capabilities=None):  # noqa: E501
        """RoleModel - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._capabilities = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if capabilities is not None:
            self.capabilities = capabilities

    @property
    def name(self):
        """Gets the name of this RoleModel.  # noqa: E501


        :return: The name of this RoleModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoleModel.


        :param name: The name of this RoleModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def capabilities(self):
        """Gets the capabilities of this RoleModel.  # noqa: E501


        :return: The capabilities of this RoleModel.  # noqa: E501
        :rtype: list[CapabilitiesModel]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this RoleModel.


        :param capabilities: The capabilities of this RoleModel.  # noqa: E501
        :type: list[CapabilitiesModel]
        """

        self._capabilities = capabilities

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
        if issubclass(RoleModel, dict):
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
        if not isinstance(other, RoleModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
