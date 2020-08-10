# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PtsV2PaymentsCapturesPost201ResponseProcessingInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'enhanced_data_enabled': 'bool'
    }

    attribute_map = {
        'enhanced_data_enabled': 'enhancedDataEnabled'
    }

    def __init__(self, enhanced_data_enabled=None):
        """
        PtsV2PaymentsCapturesPost201ResponseProcessingInformation - a model defined in Swagger
        """

        self._enhanced_data_enabled = None

        if enhanced_data_enabled is not None:
          self.enhanced_data_enabled = enhanced_data_enabled

    @property
    def enhanced_data_enabled(self):
        """
        Gets the enhanced_data_enabled of this PtsV2PaymentsCapturesPost201ResponseProcessingInformation.
        The possible values for the reply field are: - `true` : the airline data was included in the request to the processor. - `false` : the airline data was not included in the request to the processor.  Returned by authorization, capture, or credit services. 

        :return: The enhanced_data_enabled of this PtsV2PaymentsCapturesPost201ResponseProcessingInformation.
        :rtype: bool
        """
        return self._enhanced_data_enabled

    @enhanced_data_enabled.setter
    def enhanced_data_enabled(self, enhanced_data_enabled):
        """
        Sets the enhanced_data_enabled of this PtsV2PaymentsCapturesPost201ResponseProcessingInformation.
        The possible values for the reply field are: - `true` : the airline data was included in the request to the processor. - `false` : the airline data was not included in the request to the processor.  Returned by authorization, capture, or credit services. 

        :param enhanced_data_enabled: The enhanced_data_enabled of this PtsV2PaymentsCapturesPost201ResponseProcessingInformation.
        :type: bool
        """

        self._enhanced_data_enabled = enhanced_data_enabled

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PtsV2PaymentsCapturesPost201ResponseProcessingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
