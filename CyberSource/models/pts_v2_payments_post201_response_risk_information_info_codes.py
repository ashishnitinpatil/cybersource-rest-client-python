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


class PtsV2PaymentsPost201ResponseRiskInformationInfoCodes(object):
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
        'velocity': 'list[str]',
        'address': 'list[str]',
        'customer_list': 'list[str]',
        'identity_change': 'list[str]',
        'internet': 'list[str]',
        'phone': 'list[str]',
        'suspicious': 'list[str]',
        'global_velocity': 'list[str]'
    }

    attribute_map = {
        'velocity': 'velocity',
        'address': 'address',
        'customer_list': 'customerList',
        'identity_change': 'identityChange',
        'internet': 'internet',
        'phone': 'phone',
        'suspicious': 'suspicious',
        'global_velocity': 'globalVelocity'
    }

    def __init__(self, velocity=None, address=None, customer_list=None, identity_change=None, internet=None, phone=None, suspicious=None, global_velocity=None):
        """
        PtsV2PaymentsPost201ResponseRiskInformationInfoCodes - a model defined in Swagger
        """

        self._velocity = None
        self._address = None
        self._customer_list = None
        self._identity_change = None
        self._internet = None
        self._phone = None
        self._suspicious = None
        self._global_velocity = None

        if velocity is not None:
          self.velocity = velocity
        if address is not None:
          self.address = address
        if customer_list is not None:
          self.customer_list = customer_list
        if identity_change is not None:
          self.identity_change = identity_change
        if internet is not None:
          self.internet = internet
        if phone is not None:
          self.phone = phone
        if suspicious is not None:
          self.suspicious = suspicious
        if global_velocity is not None:
          self.global_velocity = global_velocity

    @property
    def velocity(self):
        """
        Gets the velocity of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        List of information codes triggered by the order. These information codes were generated when you created the order and product velocity rules and are returned so that you can associate them with the rules.  Returned by Decision Manager service. 

        :return: The velocity of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        :rtype: list[str]
        """
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        """
        Sets the velocity of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        List of information codes triggered by the order. These information codes were generated when you created the order and product velocity rules and are returned so that you can associate them with the rules.  Returned by Decision Manager service. 

        :param velocity: The velocity of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        :type: list[str]
        """

        self._velocity = velocity

    @property
    def address(self):
        """
        Gets the address of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        Indicates a mismatch between the customer’s billing and shipping addresses.  Returned by scoring service. 

        :return: The address of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        :rtype: list[str]
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        Indicates a mismatch between the customer’s billing and shipping addresses.  Returned by scoring service. 

        :param address: The address of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        :type: list[str]
        """

        self._address = address

    @property
    def customer_list(self):
        """
        Gets the customer_list of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        Indicates that customer information is associated with transactions that are either on the negative or the positive list.  Returned by scoring service. 

        :return: The customer_list of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        :rtype: list[str]
        """
        return self._customer_list

    @customer_list.setter
    def customer_list(self, customer_list):
        """
        Sets the customer_list of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        Indicates that customer information is associated with transactions that are either on the negative or the positive list.  Returned by scoring service. 

        :param customer_list: The customer_list of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        :type: list[str]
        """

        self._customer_list = customer_list

    @property
    def identity_change(self):
        """
        Gets the identity_change of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        Indicates excessive identity changes. The threshold is variable depending on the identity elements being compared. This field can contain one or more information codes, separated by carets (^).  Returned by scoring service. 

        :return: The identity_change of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        :rtype: list[str]
        """
        return self._identity_change

    @identity_change.setter
    def identity_change(self, identity_change):
        """
        Sets the identity_change of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        Indicates excessive identity changes. The threshold is variable depending on the identity elements being compared. This field can contain one or more information codes, separated by carets (^).  Returned by scoring service. 

        :param identity_change: The identity_change of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        :type: list[str]
        """

        self._identity_change = identity_change

    @property
    def internet(self):
        """
        Gets the internet of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        Indicates a problem with the customer’s email address, IP address, or billing address.  Returned by scoring service. 

        :return: The internet of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        :rtype: list[str]
        """
        return self._internet

    @internet.setter
    def internet(self, internet):
        """
        Sets the internet of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        Indicates a problem with the customer’s email address, IP address, or billing address.  Returned by scoring service. 

        :param internet: The internet of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        :type: list[str]
        """

        self._internet = internet

    @property
    def phone(self):
        """
        Gets the phone of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        Indicates a problem with the customer’s phone number.  Returned by scoring service. 

        :return: The phone of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        :rtype: list[str]
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        Indicates a problem with the customer’s phone number.  Returned by scoring service. 

        :param phone: The phone of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        :type: list[str]
        """

        self._phone = phone

    @property
    def suspicious(self):
        """
        Gets the suspicious of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        Indicates that the customer provided potentially suspicious information.  Returned by scoring service. 

        :return: The suspicious of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        :rtype: list[str]
        """
        return self._suspicious

    @suspicious.setter
    def suspicious(self, suspicious):
        """
        Sets the suspicious of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        Indicates that the customer provided potentially suspicious information.  Returned by scoring service. 

        :param suspicious: The suspicious of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        :type: list[str]
        """

        self._suspicious = suspicious

    @property
    def global_velocity(self):
        """
        Gets the global_velocity of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        Indicates that the customer has a high purchase frequency.  Returned by scoring service. 

        :return: The global_velocity of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        :rtype: list[str]
        """
        return self._global_velocity

    @global_velocity.setter
    def global_velocity(self, global_velocity):
        """
        Sets the global_velocity of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        Indicates that the customer has a high purchase frequency.  Returned by scoring service. 

        :param global_velocity: The global_velocity of this PtsV2PaymentsPost201ResponseRiskInformationInfoCodes.
        :type: list[str]
        """

        self._global_velocity = global_velocity

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseRiskInformationInfoCodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other