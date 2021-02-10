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

class FeatureSetVersionDefJob(object):
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
        'kind': 'str',
        'name': 'str',
        'runid': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'name': 'name',
        'runid': 'runid'
    }

    def __init__(self, kind=None, name=None, runid=None):  # noqa: E501
        """FeatureSetVersionDefJob - a model defined in Swagger"""  # noqa: E501
        self._kind = None
        self._name = None
        self._runid = None
        self.discriminator = None
        if kind is not None:
            self.kind = kind
        if name is not None:
            self.name = name
        if runid is not None:
            self.runid = runid

    @property
    def kind(self):
        """Gets the kind of this FeatureSetVersionDefJob.  # noqa: E501


        :return: The kind of this FeatureSetVersionDefJob.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this FeatureSetVersionDefJob.


        :param kind: The kind of this FeatureSetVersionDefJob.  # noqa: E501
        :type: str
        """
        allowed_values = ["pipeline", "dkube_run"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this FeatureSetVersionDefJob.  # noqa: E501

        UUID of the job/pipeline which created this featureset  # noqa: E501

        :return: The name of this FeatureSetVersionDefJob.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeatureSetVersionDefJob.

        UUID of the job/pipeline which created this featureset  # noqa: E501

        :param name: The name of this FeatureSetVersionDefJob.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def runid(self):
        """Gets the runid of this FeatureSetVersionDefJob.  # noqa: E501


        :return: The runid of this FeatureSetVersionDefJob.  # noqa: E501
        :rtype: str
        """
        return self._runid

    @runid.setter
    def runid(self, runid):
        """Sets the runid of this FeatureSetVersionDefJob.


        :param runid: The runid of this FeatureSetVersionDefJob.  # noqa: E501
        :type: str
        """

        self._runid = runid

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
        if issubclass(FeatureSetVersionDefJob, dict):
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
        if not isinstance(other, FeatureSetVersionDefJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
