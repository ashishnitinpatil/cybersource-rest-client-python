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


class Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformationService(object):
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
        'category_code': 'str',
        'sub_category_code': 'str'
    }

    attribute_map = {
        'category_code': 'categoryCode',
        'sub_category_code': 'subCategoryCode'
    }

    def __init__(self, category_code=None, sub_category_code=None):
        """
        Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformationService - a model defined in Swagger
        """

        self._category_code = None
        self._sub_category_code = None

        if category_code is not None:
          self.category_code = category_code
        if sub_category_code is not None:
          self.sub_category_code = sub_category_code

    @property
    def category_code(self):
        """
        Gets the category_code of this Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformationService.
        Category code for the ancillary service that is provided. Obtain the codes from the International Air Transport Association (IATA). **Note** `#` is either 0, 1, 2, or 3. **Important** This field is required in the U.S. in order for you to qualify for either the custom payment service (CPS) or the electronic interchange reimbursement fee (EIRF)program. Format: English characters only. Optional request field for ancillary services. 

        :return: The category_code of this Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformationService.
        :rtype: str
        """
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        """
        Sets the category_code of this Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformationService.
        Category code for the ancillary service that is provided. Obtain the codes from the International Air Transport Association (IATA). **Note** `#` is either 0, 1, 2, or 3. **Important** This field is required in the U.S. in order for you to qualify for either the custom payment service (CPS) or the electronic interchange reimbursement fee (EIRF)program. Format: English characters only. Optional request field for ancillary services. 

        :param category_code: The category_code of this Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformationService.
        :type: str
        """
        if category_code is not None and len(category_code) > 4:
            raise ValueError("Invalid value for `category_code`, length must be less than or equal to `4`")

        self._category_code = category_code

    @property
    def sub_category_code(self):
        """
        Gets the sub_category_code of this Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformationService.
        Subcategory code for the ancillary service category. Obtain the codes from the International Air Transport Association (IATA). **Note** `#` is either 0, 1, 2, or 3. Format  English characters only. Optional request field for ancillary services. 

        :return: The sub_category_code of this Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformationService.
        :rtype: str
        """
        return self._sub_category_code

    @sub_category_code.setter
    def sub_category_code(self, sub_category_code):
        """
        Sets the sub_category_code of this Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformationService.
        Subcategory code for the ancillary service category. Obtain the codes from the International Air Transport Association (IATA). **Note** `#` is either 0, 1, 2, or 3. Format  English characters only. Optional request field for ancillary services. 

        :param sub_category_code: The sub_category_code of this Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformationService.
        :type: str
        """
        if sub_category_code is not None and len(sub_category_code) > 4:
            raise ValueError("Invalid value for `sub_category_code`, length must be less than or equal to `4`")

        self._sub_category_code = sub_category_code

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
        if not isinstance(other, Ptsv2paymentsTravelInformationTransitAirlineAncillaryInformationService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other