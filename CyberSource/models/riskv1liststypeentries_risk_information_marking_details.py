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


class Riskv1liststypeentriesRiskInformationMarkingDetails(object):
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
        'notes': 'str',
        'reason': 'str',
        'record_name': 'str',
        'action': 'str'
    }

    attribute_map = {
        'notes': 'notes',
        'reason': 'reason',
        'record_name': 'recordName',
        'action': 'action'
    }

    def __init__(self, notes=None, reason=None, record_name=None, action=None):
        """
        Riskv1liststypeentriesRiskInformationMarkingDetails - a model defined in Swagger
        """

        self._notes = None
        self._reason = None
        self._record_name = None
        self._action = None

        if notes is not None:
          self.notes = notes
        if reason is not None:
          self.reason = reason
        if record_name is not None:
          self.record_name = record_name
        if action is not None:
          self.action = action

    @property
    def notes(self):
        """
        Gets the notes of this Riskv1liststypeentriesRiskInformationMarkingDetails.
        Notes or details that explain the reasons for adding the transaction to either the positive or negative list.

        :return: The notes of this Riskv1liststypeentriesRiskInformationMarkingDetails.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this Riskv1liststypeentriesRiskInformationMarkingDetails.
        Notes or details that explain the reasons for adding the transaction to either the positive or negative list.

        :param notes: The notes of this Riskv1liststypeentriesRiskInformationMarkingDetails.
        :type: str
        """
        if notes is not None and len(notes) > 120:
            raise ValueError("Invalid value for `notes`, length must be less than or equal to `120`")

        self._notes = notes

    @property
    def reason(self):
        """
        Gets the reason of this Riskv1liststypeentriesRiskInformationMarkingDetails.
        Reason for adding the transaction to the negative list. This field can contain one of the following values: - `fraud_chargeback:` You have received a fraud-related chargeback for the transaction. - `non_fraud_chargeback:` You have received a non-fraudulent chargeback for the transaction. - `suspected:` You believe that you will probably receive a chargeback for the transaction. - `creditback:` You issued a refund to the customer to avoid a chargeback for the transaction. 

        :return: The reason of this Riskv1liststypeentriesRiskInformationMarkingDetails.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this Riskv1liststypeentriesRiskInformationMarkingDetails.
        Reason for adding the transaction to the negative list. This field can contain one of the following values: - `fraud_chargeback:` You have received a fraud-related chargeback for the transaction. - `non_fraud_chargeback:` You have received a non-fraudulent chargeback for the transaction. - `suspected:` You believe that you will probably receive a chargeback for the transaction. - `creditback:` You issued a refund to the customer to avoid a chargeback for the transaction. 

        :param reason: The reason of this Riskv1liststypeentriesRiskInformationMarkingDetails.
        :type: str
        """
        if reason is not None and len(reason) > 25:
            raise ValueError("Invalid value for `reason`, length must be less than or equal to `25`")

        self._reason = reason

    @property
    def record_name(self):
        """
        Gets the record_name of this Riskv1liststypeentriesRiskInformationMarkingDetails.
        Name of the customer’s record entered in the list. For the positive list, it is required if `action_ code`=`add_positive`. If absent from the request, `ics_risk_update` creates the value for this field by concatenating the customer’s first and last names. For the negative and the review lists, `record_name`, `customer_firstname`, and `customer_lastname` are optional. 

        :return: The record_name of this Riskv1liststypeentriesRiskInformationMarkingDetails.
        :rtype: str
        """
        return self._record_name

    @record_name.setter
    def record_name(self, record_name):
        """
        Sets the record_name of this Riskv1liststypeentriesRiskInformationMarkingDetails.
        Name of the customer’s record entered in the list. For the positive list, it is required if `action_ code`=`add_positive`. If absent from the request, `ics_risk_update` creates the value for this field by concatenating the customer’s first and last names. For the negative and the review lists, `record_name`, `customer_firstname`, and `customer_lastname` are optional. 

        :param record_name: The record_name of this Riskv1liststypeentriesRiskInformationMarkingDetails.
        :type: str
        """
        if record_name is not None and len(record_name) > 255:
            raise ValueError("Invalid value for `record_name`, length must be less than or equal to `255`")

        self._record_name = record_name

    @property
    def action(self):
        """
        Gets the action of this Riskv1liststypeentriesRiskInformationMarkingDetails.
        Indicates whether to add to or remove a customer’s identity from the negative or positive list. This field can contain one of the following values: - add: Add information to the list. - convert: moves the data. - delete: deletes the data from the list. 

        :return: The action of this Riskv1liststypeentriesRiskInformationMarkingDetails.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this Riskv1liststypeentriesRiskInformationMarkingDetails.
        Indicates whether to add to or remove a customer’s identity from the negative or positive list. This field can contain one of the following values: - add: Add information to the list. - convert: moves the data. - delete: deletes the data from the list. 

        :param action: The action of this Riskv1liststypeentriesRiskInformationMarkingDetails.
        :type: str
        """

        self._action = action

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
        if not isinstance(other, Riskv1liststypeentriesRiskInformationMarkingDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
