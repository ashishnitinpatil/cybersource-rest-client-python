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


class TssV2TransactionsPost201ResponseEmbeddedPaymentInformationPaymentType(object):
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
        'type': 'str',
        'method': 'str'
    }

    attribute_map = {
        'type': 'type',
        'method': 'method'
    }

    def __init__(self, type=None, method=None):
        """
        TssV2TransactionsPost201ResponseEmbeddedPaymentInformationPaymentType - a model defined in Swagger
        """

        self._type = None
        self._method = None

        if type is not None:
          self.type = type
        if method is not None:
          self.method = method

    @property
    def type(self):
        """
        Gets the type of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationPaymentType.
        Indicates the payment type used in this payment transaction. Example: credit card, check

        :return: The type of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationPaymentType.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationPaymentType.
        Indicates the payment type used in this payment transaction. Example: credit card, check

        :param type: The type of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationPaymentType.
        :type: str
        """

        self._type = type

    @property
    def method(self):
        """
        Gets the method of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationPaymentType.
        Indicates the payment method used in this payment transaction.

        :return: The method of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationPaymentType.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationPaymentType.
        Indicates the payment method used in this payment transaction.

        :param method: The method of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationPaymentType.
        :type: str
        """

        self._method = method

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
        if not isinstance(other, TssV2TransactionsPost201ResponseEmbeddedPaymentInformationPaymentType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
