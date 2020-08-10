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


class Tmsv2customersBuyerInformation(object):
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
        'merchant_customer_id': 'str',
        'email': 'str'
    }

    attribute_map = {
        'merchant_customer_id': 'merchantCustomerID',
        'email': 'email'
    }

    def __init__(self, merchant_customer_id=None, email=None):
        """
        Tmsv2customersBuyerInformation - a model defined in Swagger
        """

        self._merchant_customer_id = None
        self._email = None

        if merchant_customer_id is not None:
          self.merchant_customer_id = merchant_customer_id
        if email is not None:
          self.email = email

    @property
    def merchant_customer_id(self):
        """
        Gets the merchant_customer_id of this Tmsv2customersBuyerInformation.
        Your identifier for the customer. 

        :return: The merchant_customer_id of this Tmsv2customersBuyerInformation.
        :rtype: str
        """
        return self._merchant_customer_id

    @merchant_customer_id.setter
    def merchant_customer_id(self, merchant_customer_id):
        """
        Sets the merchant_customer_id of this Tmsv2customersBuyerInformation.
        Your identifier for the customer. 

        :param merchant_customer_id: The merchant_customer_id of this Tmsv2customersBuyerInformation.
        :type: str
        """
        if merchant_customer_id is not None and len(merchant_customer_id) > 100:
            raise ValueError("Invalid value for `merchant_customer_id`, length must be less than or equal to `100`")

        self._merchant_customer_id = merchant_customer_id

    @property
    def email(self):
        """
        Gets the email of this Tmsv2customersBuyerInformation.
        Customer's primary email address, including the full domain name. 

        :return: The email of this Tmsv2customersBuyerInformation.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Tmsv2customersBuyerInformation.
        Customer's primary email address, including the full domain name. 

        :param email: The email of this Tmsv2customersBuyerInformation.
        :type: str
        """
        if email is not None and len(email) > 255:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `255`")

        self._email = email

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
        if not isinstance(other, Tmsv2customersBuyerInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other