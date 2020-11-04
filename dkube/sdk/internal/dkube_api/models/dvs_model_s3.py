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


class ModelS3(object):
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
        'bucket': 'str',
        'secretid': 'str',
        'secretkey': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'secretid': 'secretid',
        'secretkey': 'secretkey'
    }

    def __init__(self, bucket=None, secretid=None, secretkey=None):  # noqa: E501
        """ModelS3 - a model defined in Swagger"""  # noqa: E501

        self._bucket = None
        self._secretid = None
        self._secretkey = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        if secretid is not None:
            self.secretid = secretid
        if secretkey is not None:
            self.secretkey = secretkey

    @property
    def bucket(self):
        """Gets the bucket of this ModelS3.  # noqa: E501


        :return: The bucket of this ModelS3.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this ModelS3.


        :param bucket: The bucket of this ModelS3.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def secretid(self):
        """Gets the secretid of this ModelS3.  # noqa: E501


        :return: The secretid of this ModelS3.  # noqa: E501
        :rtype: str
        """
        return self._secretid

    @secretid.setter
    def secretid(self, secretid):
        """Sets the secretid of this ModelS3.


        :param secretid: The secretid of this ModelS3.  # noqa: E501
        :type: str
        """

        self._secretid = secretid

    @property
    def secretkey(self):
        """Gets the secretkey of this ModelS3.  # noqa: E501


        :return: The secretkey of this ModelS3.  # noqa: E501
        :rtype: str
        """
        return self._secretkey

    @secretkey.setter
    def secretkey(self, secretkey):
        """Sets the secretkey of this ModelS3.


        :param secretkey: The secretkey of this ModelS3.  # noqa: E501
        :type: str
        """

        self._secretkey = secretkey

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
        if issubclass(ModelS3, dict):
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
        if not isinstance(other, ModelS3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
