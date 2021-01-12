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


class JobModelParameters(object):
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
        '_class': 'str',
        'gpu_allocation': 'GpuAllocation',
        'priority': 'RunTemplateModelParametersPriority',
        'training': 'DSJobModel',
        'notebook': 'DSJobModel',
        'inference': 'InferenceJobModel',
        'preprocessing': 'PreprocessingJobModel',
        'custom': 'CustomJobModel',
        'run': 'JobModelParametersRun',
        'generated': 'JobModelParametersGenerated'
    }

    attribute_map = {
        '_class': 'class',
        'gpu_allocation': 'gpu_allocation',
        'priority': 'priority',
        'training': 'training',
        'notebook': 'notebook',
        'inference': 'inference',
        'preprocessing': 'preprocessing',
        'custom': 'custom',
        'run': 'run',
        'generated': 'generated'
    }

    def __init__(self, _class=None, gpu_allocation=None, priority=None, training=None, notebook=None, inference=None, preprocessing=None, custom=None, run=None, generated=None):  # noqa: E501
        """JobModelParameters - a model defined in Swagger"""  # noqa: E501

        self.__class = None
        self._gpu_allocation = None
        self._priority = None
        self._training = None
        self._notebook = None
        self._inference = None
        self._preprocessing = None
        self._custom = None
        self._run = None
        self._generated = None
        self.discriminator = None

        if _class is not None:
            self._class = _class
        if gpu_allocation is not None:
            self.gpu_allocation = gpu_allocation
        if priority is not None:
            self.priority = priority
        if training is not None:
            self.training = training
        if notebook is not None:
            self.notebook = notebook
        if inference is not None:
            self.inference = inference
        if preprocessing is not None:
            self.preprocessing = preprocessing
        if custom is not None:
            self.custom = custom
        if run is not None:
            self.run = run
        if generated is not None:
            self.generated = generated

    @property
    def _class(self):
        """Gets the _class of this JobModelParameters.  # noqa: E501


        :return: The _class of this JobModelParameters.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this JobModelParameters.


        :param _class: The _class of this JobModelParameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["training", "notebook", "inference", "preprocessing", "custom", "rstudio"]  # noqa: E501
        if _class not in allowed_values:
            raise ValueError(
                "Invalid value for `_class` ({0}), must be one of {1}"  # noqa: E501
                .format(_class, allowed_values)
            )

        self.__class = _class

    @property
    def gpu_allocation(self):
        """Gets the gpu_allocation of this JobModelParameters.  # noqa: E501


        :return: The gpu_allocation of this JobModelParameters.  # noqa: E501
        :rtype: GpuAllocation
        """
        return self._gpu_allocation

    @gpu_allocation.setter
    def gpu_allocation(self, gpu_allocation):
        """Sets the gpu_allocation of this JobModelParameters.


        :param gpu_allocation: The gpu_allocation of this JobModelParameters.  # noqa: E501
        :type: GpuAllocation
        """

        self._gpu_allocation = gpu_allocation

    @property
    def priority(self):
        """Gets the priority of this JobModelParameters.  # noqa: E501


        :return: The priority of this JobModelParameters.  # noqa: E501
        :rtype: RunTemplateModelParametersPriority
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this JobModelParameters.


        :param priority: The priority of this JobModelParameters.  # noqa: E501
        :type: RunTemplateModelParametersPriority
        """

        self._priority = priority

    @property
    def training(self):
        """Gets the training of this JobModelParameters.  # noqa: E501

        Training job related inputs. Should be provided if choice is training job.  # noqa: E501

        :return: The training of this JobModelParameters.  # noqa: E501
        :rtype: DSJobModel
        """
        return self._training

    @training.setter
    def training(self, training):
        """Sets the training of this JobModelParameters.

        Training job related inputs. Should be provided if choice is training job.  # noqa: E501

        :param training: The training of this JobModelParameters.  # noqa: E501
        :type: DSJobModel
        """

        self._training = training

    @property
    def notebook(self):
        """Gets the notebook of this JobModelParameters.  # noqa: E501

        Notebook job related inputs. Should be provided if choice is notebook job.  # noqa: E501

        :return: The notebook of this JobModelParameters.  # noqa: E501
        :rtype: DSJobModel
        """
        return self._notebook

    @notebook.setter
    def notebook(self, notebook):
        """Sets the notebook of this JobModelParameters.

        Notebook job related inputs. Should be provided if choice is notebook job.  # noqa: E501

        :param notebook: The notebook of this JobModelParameters.  # noqa: E501
        :type: DSJobModel
        """

        self._notebook = notebook

    @property
    def inference(self):
        """Gets the inference of this JobModelParameters.  # noqa: E501

        Inference job related inputs. Should be provided if choice is inference job.  # noqa: E501

        :return: The inference of this JobModelParameters.  # noqa: E501
        :rtype: InferenceJobModel
        """
        return self._inference

    @inference.setter
    def inference(self, inference):
        """Sets the inference of this JobModelParameters.

        Inference job related inputs. Should be provided if choice is inference job.  # noqa: E501

        :param inference: The inference of this JobModelParameters.  # noqa: E501
        :type: InferenceJobModel
        """

        self._inference = inference

    @property
    def preprocessing(self):
        """Gets the preprocessing of this JobModelParameters.  # noqa: E501

        Data processing job related inputs. Should be provided if choice is data job. Job which downloads/does some processing on available data and generates new dataset for further consumption.  # noqa: E501

        :return: The preprocessing of this JobModelParameters.  # noqa: E501
        :rtype: PreprocessingJobModel
        """
        return self._preprocessing

    @preprocessing.setter
    def preprocessing(self, preprocessing):
        """Sets the preprocessing of this JobModelParameters.

        Data processing job related inputs. Should be provided if choice is data job. Job which downloads/does some processing on available data and generates new dataset for further consumption.  # noqa: E501

        :param preprocessing: The preprocessing of this JobModelParameters.  # noqa: E501
        :type: PreprocessingJobModel
        """

        self._preprocessing = preprocessing

    @property
    def custom(self):
        """Gets the custom of this JobModelParameters.  # noqa: E501

        Custom job related inputs. Should be provided if choice is custom. Job which does custom tasks.  # noqa: E501

        :return: The custom of this JobModelParameters.  # noqa: E501
        :rtype: CustomJobModel
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this JobModelParameters.

        Custom job related inputs. Should be provided if choice is custom. Job which does custom tasks.  # noqa: E501

        :param custom: The custom of this JobModelParameters.  # noqa: E501
        :type: CustomJobModel
        """

        self._custom = custom

    @property
    def run(self):
        """Gets the run of this JobModelParameters.  # noqa: E501


        :return: The run of this JobModelParameters.  # noqa: E501
        :rtype: JobModelParametersRun
        """
        return self._run

    @run.setter
    def run(self, run):
        """Sets the run of this JobModelParameters.


        :param run: The run of this JobModelParameters.  # noqa: E501
        :type: JobModelParametersRun
        """

        self._run = run

    @property
    def generated(self):
        """Gets the generated of this JobModelParameters.  # noqa: E501


        :return: The generated of this JobModelParameters.  # noqa: E501
        :rtype: JobModelParametersGenerated
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this JobModelParameters.


        :param generated: The generated of this JobModelParameters.  # noqa: E501
        :type: JobModelParametersGenerated
        """

        self._generated = generated

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
        if issubclass(JobModelParameters, dict):
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
        if not isinstance(other, JobModelParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
