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


class Kmsv2keyssymClientReferenceInformation(object):
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
        'code': 'str',
        'comments': 'str',
        'partner': 'Vasv2taxClientReferenceInformationPartner'
    }

    attribute_map = {
        'code': 'code',
        'comments': 'comments',
        'partner': 'partner'
    }

    def __init__(self, code=None, comments=None, partner=None):
        """
        Kmsv2keyssymClientReferenceInformation - a model defined in Swagger
        """

        self._code = None
        self._comments = None
        self._partner = None

        if code is not None:
          self.code = code
        if comments is not None:
          self.comments = comments
        if partner is not None:
          self.partner = partner

    @property
    def code(self):
        """
        Gets the code of this Kmsv2keyssymClientReferenceInformation.
        Client-generated order reference or tracking number. CyberSource recommends that you send a unique value. 

        :return: The code of this Kmsv2keyssymClientReferenceInformation.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Kmsv2keyssymClientReferenceInformation.
        Client-generated order reference or tracking number. CyberSource recommends that you send a unique value. 

        :param code: The code of this Kmsv2keyssymClientReferenceInformation.
        :type: str
        """
        if code is not None and len(code) > 50:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `50`")

        self._code = code

    @property
    def comments(self):
        """
        Gets the comments of this Kmsv2keyssymClientReferenceInformation.
        Comments

        :return: The comments of this Kmsv2keyssymClientReferenceInformation.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this Kmsv2keyssymClientReferenceInformation.
        Comments

        :param comments: The comments of this Kmsv2keyssymClientReferenceInformation.
        :type: str
        """

        self._comments = comments

    @property
    def partner(self):
        """
        Gets the partner of this Kmsv2keyssymClientReferenceInformation.

        :return: The partner of this Kmsv2keyssymClientReferenceInformation.
        :rtype: Vasv2taxClientReferenceInformationPartner
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """
        Sets the partner of this Kmsv2keyssymClientReferenceInformation.

        :param partner: The partner of this Kmsv2keyssymClientReferenceInformation.
        :type: Vasv2taxClientReferenceInformationPartner
        """

        self._partner = partner

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
        if not isinstance(other, Kmsv2keyssymClientReferenceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other