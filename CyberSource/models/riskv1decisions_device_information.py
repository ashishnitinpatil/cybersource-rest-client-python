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


class Riskv1decisionsDeviceInformation(object):
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
        'cookies_accepted': 'str',
        'ip_address': 'str',
        'host_name': 'str',
        'fingerprint_session_id': 'str',
        'http_browser_email': 'str',
        'user_agent': 'str',
        'raw_data': 'list[Ptsv2paymentsDeviceInformationRawData]',
        'http_accept_browser_value': 'str',
        'http_accept_content': 'str',
        'http_browser_language': 'str',
        'http_browser_java_enabled': 'bool',
        'http_browser_java_script_enabled': 'bool',
        'http_browser_color_depth': 'str',
        'http_browser_screen_height': 'str',
        'http_browser_screen_width': 'str',
        'http_browser_time_difference': 'str',
        'user_agent_browser_value': 'str'
    }

    attribute_map = {
        'cookies_accepted': 'cookiesAccepted',
        'ip_address': 'ipAddress',
        'host_name': 'hostName',
        'fingerprint_session_id': 'fingerprintSessionId',
        'http_browser_email': 'httpBrowserEmail',
        'user_agent': 'userAgent',
        'raw_data': 'rawData',
        'http_accept_browser_value': 'httpAcceptBrowserValue',
        'http_accept_content': 'httpAcceptContent',
        'http_browser_language': 'httpBrowserLanguage',
        'http_browser_java_enabled': 'httpBrowserJavaEnabled',
        'http_browser_java_script_enabled': 'httpBrowserJavaScriptEnabled',
        'http_browser_color_depth': 'httpBrowserColorDepth',
        'http_browser_screen_height': 'httpBrowserScreenHeight',
        'http_browser_screen_width': 'httpBrowserScreenWidth',
        'http_browser_time_difference': 'httpBrowserTimeDifference',
        'user_agent_browser_value': 'userAgentBrowserValue'
    }

    def __init__(self, cookies_accepted=None, ip_address=None, host_name=None, fingerprint_session_id=None, http_browser_email=None, user_agent=None, raw_data=None, http_accept_browser_value=None, http_accept_content=None, http_browser_language=None, http_browser_java_enabled=None, http_browser_java_script_enabled=None, http_browser_color_depth=None, http_browser_screen_height=None, http_browser_screen_width=None, http_browser_time_difference=None, user_agent_browser_value=None):
        """
        Riskv1decisionsDeviceInformation - a model defined in Swagger
        """

        self._cookies_accepted = None
        self._ip_address = None
        self._host_name = None
        self._fingerprint_session_id = None
        self._http_browser_email = None
        self._user_agent = None
        self._raw_data = None
        self._http_accept_browser_value = None
        self._http_accept_content = None
        self._http_browser_language = None
        self._http_browser_java_enabled = None
        self._http_browser_java_script_enabled = None
        self._http_browser_color_depth = None
        self._http_browser_screen_height = None
        self._http_browser_screen_width = None
        self._http_browser_time_difference = None
        self._user_agent_browser_value = None

        if cookies_accepted is not None:
          self.cookies_accepted = cookies_accepted
        if ip_address is not None:
          self.ip_address = ip_address
        if host_name is not None:
          self.host_name = host_name
        if fingerprint_session_id is not None:
          self.fingerprint_session_id = fingerprint_session_id
        if http_browser_email is not None:
          self.http_browser_email = http_browser_email
        if user_agent is not None:
          self.user_agent = user_agent
        if raw_data is not None:
          self.raw_data = raw_data
        if http_accept_browser_value is not None:
          self.http_accept_browser_value = http_accept_browser_value
        if http_accept_content is not None:
          self.http_accept_content = http_accept_content
        if http_browser_language is not None:
          self.http_browser_language = http_browser_language
        if http_browser_java_enabled is not None:
          self.http_browser_java_enabled = http_browser_java_enabled
        if http_browser_java_script_enabled is not None:
          self.http_browser_java_script_enabled = http_browser_java_script_enabled
        if http_browser_color_depth is not None:
          self.http_browser_color_depth = http_browser_color_depth
        if http_browser_screen_height is not None:
          self.http_browser_screen_height = http_browser_screen_height
        if http_browser_screen_width is not None:
          self.http_browser_screen_width = http_browser_screen_width
        if http_browser_time_difference is not None:
          self.http_browser_time_difference = http_browser_time_difference
        if user_agent_browser_value is not None:
          self.user_agent_browser_value = user_agent_browser_value

    @property
    def cookies_accepted(self):
        """
        Gets the cookies_accepted of this Riskv1decisionsDeviceInformation.
        Whether the customer’s browser accepts cookies. This field can contain one of the following values: - `yes`: The customer’s browser accepts cookies. - `no`: The customer’s browser does not accept cookies. 

        :return: The cookies_accepted of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._cookies_accepted

    @cookies_accepted.setter
    def cookies_accepted(self, cookies_accepted):
        """
        Sets the cookies_accepted of this Riskv1decisionsDeviceInformation.
        Whether the customer’s browser accepts cookies. This field can contain one of the following values: - `yes`: The customer’s browser accepts cookies. - `no`: The customer’s browser does not accept cookies. 

        :param cookies_accepted: The cookies_accepted of this Riskv1decisionsDeviceInformation.
        :type: str
        """

        self._cookies_accepted = cookies_accepted

    @property
    def ip_address(self):
        """
        Gets the ip_address of this Riskv1decisionsDeviceInformation.
        IP address of the customer.  #### Used by **Authorization, Capture, and Credit** Optional field. 

        :return: The ip_address of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Riskv1decisionsDeviceInformation.
        IP address of the customer.  #### Used by **Authorization, Capture, and Credit** Optional field. 

        :param ip_address: The ip_address of this Riskv1decisionsDeviceInformation.
        :type: str
        """
        if ip_address is not None and len(ip_address) > 48:
            raise ValueError("Invalid value for `ip_address`, length must be less than or equal to `48`")

        self._ip_address = ip_address

    @property
    def host_name(self):
        """
        Gets the host_name of this Riskv1decisionsDeviceInformation.
        DNS resolved hostname from `ipAddress`.

        :return: The host_name of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this Riskv1decisionsDeviceInformation.
        DNS resolved hostname from `ipAddress`.

        :param host_name: The host_name of this Riskv1decisionsDeviceInformation.
        :type: str
        """
        if host_name is not None and len(host_name) > 60:
            raise ValueError("Invalid value for `host_name`, length must be less than or equal to `60`")

        self._host_name = host_name

    @property
    def fingerprint_session_id(self):
        """
        Gets the fingerprint_session_id of this Riskv1decisionsDeviceInformation.
        Field that contains the session ID that you send to Decision Manager to obtain the device fingerprint information. The string can contain uppercase and lowercase letters, digits, hyphen (-), and underscore (_). However, do not use the same uppercase and lowercase letters to indicate different session IDs.  The session ID must be unique for each merchant ID. You can use any string that you are already generating, such as an order number or web session ID.  The session ID must be unique for each page load, regardless of an individual’s web session ID. If a user navigates to a profiled page and is assigned a web session, navigates away from the profiled page, then navigates back to the profiled page, the generated session ID should be different and unique. You may use a web session ID, but it is preferable to use an application GUID (Globally Unique Identifier). This measure ensures that a unique ID is generated every time the page is loaded, even if it is the same user reloading the page. 

        :return: The fingerprint_session_id of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._fingerprint_session_id

    @fingerprint_session_id.setter
    def fingerprint_session_id(self, fingerprint_session_id):
        """
        Sets the fingerprint_session_id of this Riskv1decisionsDeviceInformation.
        Field that contains the session ID that you send to Decision Manager to obtain the device fingerprint information. The string can contain uppercase and lowercase letters, digits, hyphen (-), and underscore (_). However, do not use the same uppercase and lowercase letters to indicate different session IDs.  The session ID must be unique for each merchant ID. You can use any string that you are already generating, such as an order number or web session ID.  The session ID must be unique for each page load, regardless of an individual’s web session ID. If a user navigates to a profiled page and is assigned a web session, navigates away from the profiled page, then navigates back to the profiled page, the generated session ID should be different and unique. You may use a web session ID, but it is preferable to use an application GUID (Globally Unique Identifier). This measure ensures that a unique ID is generated every time the page is loaded, even if it is the same user reloading the page. 

        :param fingerprint_session_id: The fingerprint_session_id of this Riskv1decisionsDeviceInformation.
        :type: str
        """

        self._fingerprint_session_id = fingerprint_session_id

    @property
    def http_browser_email(self):
        """
        Gets the http_browser_email of this Riskv1decisionsDeviceInformation.
        Email address set in the customer’s browser, which may differ from customer email. 

        :return: The http_browser_email of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._http_browser_email

    @http_browser_email.setter
    def http_browser_email(self, http_browser_email):
        """
        Sets the http_browser_email of this Riskv1decisionsDeviceInformation.
        Email address set in the customer’s browser, which may differ from customer email. 

        :param http_browser_email: The http_browser_email of this Riskv1decisionsDeviceInformation.
        :type: str
        """

        self._http_browser_email = http_browser_email

    @property
    def user_agent(self):
        """
        Gets the user_agent of this Riskv1decisionsDeviceInformation.
        Customer’s browser as identified from the HTTP header data. For example, `Mozilla` is the value that identifies the Netscape browser. 

        :return: The user_agent of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """
        Sets the user_agent of this Riskv1decisionsDeviceInformation.
        Customer’s browser as identified from the HTTP header data. For example, `Mozilla` is the value that identifies the Netscape browser. 

        :param user_agent: The user_agent of this Riskv1decisionsDeviceInformation.
        :type: str
        """
        if user_agent is not None and len(user_agent) > 40:
            raise ValueError("Invalid value for `user_agent`, length must be less than or equal to `40`")

        self._user_agent = user_agent

    @property
    def raw_data(self):
        """
        Gets the raw_data of this Riskv1decisionsDeviceInformation.

        :return: The raw_data of this Riskv1decisionsDeviceInformation.
        :rtype: list[Ptsv2paymentsDeviceInformationRawData]
        """
        return self._raw_data

    @raw_data.setter
    def raw_data(self, raw_data):
        """
        Sets the raw_data of this Riskv1decisionsDeviceInformation.

        :param raw_data: The raw_data of this Riskv1decisionsDeviceInformation.
        :type: list[Ptsv2paymentsDeviceInformationRawData]
        """

        self._raw_data = raw_data

    @property
    def http_accept_browser_value(self):
        """
        Gets the http_accept_browser_value of this Riskv1decisionsDeviceInformation.
        Value of the Accept header sent by the customer’s web browser. **Note** If the customer’s browser provides a value, you must include it in your request. 

        :return: The http_accept_browser_value of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._http_accept_browser_value

    @http_accept_browser_value.setter
    def http_accept_browser_value(self, http_accept_browser_value):
        """
        Sets the http_accept_browser_value of this Riskv1decisionsDeviceInformation.
        Value of the Accept header sent by the customer’s web browser. **Note** If the customer’s browser provides a value, you must include it in your request. 

        :param http_accept_browser_value: The http_accept_browser_value of this Riskv1decisionsDeviceInformation.
        :type: str
        """
        if http_accept_browser_value is not None and len(http_accept_browser_value) > 255:
            raise ValueError("Invalid value for `http_accept_browser_value`, length must be less than or equal to `255`")

        self._http_accept_browser_value = http_accept_browser_value

    @property
    def http_accept_content(self):
        """
        Gets the http_accept_content of this Riskv1decisionsDeviceInformation.
        The exact content of the HTTP accept header. 

        :return: The http_accept_content of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._http_accept_content

    @http_accept_content.setter
    def http_accept_content(self, http_accept_content):
        """
        Sets the http_accept_content of this Riskv1decisionsDeviceInformation.
        The exact content of the HTTP accept header. 

        :param http_accept_content: The http_accept_content of this Riskv1decisionsDeviceInformation.
        :type: str
        """
        if http_accept_content is not None and len(http_accept_content) > 256:
            raise ValueError("Invalid value for `http_accept_content`, length must be less than or equal to `256`")

        self._http_accept_content = http_accept_content

    @property
    def http_browser_language(self):
        """
        Gets the http_browser_language of this Riskv1decisionsDeviceInformation.
        Value represents the browser language as defined in IETF BCP47. Example:en-US, refer  https://en.wikipedia.org/wiki/IETF_language_tag for more details. 

        :return: The http_browser_language of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._http_browser_language

    @http_browser_language.setter
    def http_browser_language(self, http_browser_language):
        """
        Sets the http_browser_language of this Riskv1decisionsDeviceInformation.
        Value represents the browser language as defined in IETF BCP47. Example:en-US, refer  https://en.wikipedia.org/wiki/IETF_language_tag for more details. 

        :param http_browser_language: The http_browser_language of this Riskv1decisionsDeviceInformation.
        :type: str
        """
        if http_browser_language is not None and len(http_browser_language) > 8:
            raise ValueError("Invalid value for `http_browser_language`, length must be less than or equal to `8`")

        self._http_browser_language = http_browser_language

    @property
    def http_browser_java_enabled(self):
        """
        Gets the http_browser_java_enabled of this Riskv1decisionsDeviceInformation.
        A Boolean value that represents the ability of the cardholder browser to execute Java. Value is returned from the navigator.javaEnabled property. Possible Values:True/False 

        :return: The http_browser_java_enabled of this Riskv1decisionsDeviceInformation.
        :rtype: bool
        """
        return self._http_browser_java_enabled

    @http_browser_java_enabled.setter
    def http_browser_java_enabled(self, http_browser_java_enabled):
        """
        Sets the http_browser_java_enabled of this Riskv1decisionsDeviceInformation.
        A Boolean value that represents the ability of the cardholder browser to execute Java. Value is returned from the navigator.javaEnabled property. Possible Values:True/False 

        :param http_browser_java_enabled: The http_browser_java_enabled of this Riskv1decisionsDeviceInformation.
        :type: bool
        """

        self._http_browser_java_enabled = http_browser_java_enabled

    @property
    def http_browser_java_script_enabled(self):
        """
        Gets the http_browser_java_script_enabled of this Riskv1decisionsDeviceInformation.
        A Boolean value that represents the ability of the cardholder browser to execute JavaScript. Possible Values:True/False. **Note**: Merchants should be able to know the values from fingerprint details of cardholder's browser. 

        :return: The http_browser_java_script_enabled of this Riskv1decisionsDeviceInformation.
        :rtype: bool
        """
        return self._http_browser_java_script_enabled

    @http_browser_java_script_enabled.setter
    def http_browser_java_script_enabled(self, http_browser_java_script_enabled):
        """
        Sets the http_browser_java_script_enabled of this Riskv1decisionsDeviceInformation.
        A Boolean value that represents the ability of the cardholder browser to execute JavaScript. Possible Values:True/False. **Note**: Merchants should be able to know the values from fingerprint details of cardholder's browser. 

        :param http_browser_java_script_enabled: The http_browser_java_script_enabled of this Riskv1decisionsDeviceInformation.
        :type: bool
        """

        self._http_browser_java_script_enabled = http_browser_java_script_enabled

    @property
    def http_browser_color_depth(self):
        """
        Gets the http_browser_color_depth of this Riskv1decisionsDeviceInformation.
        Value represents the bit depth of the color palette for displaying images, in bits per pixel. Example : 24, refer https://en.wikipedia.org/wiki/Color_depth for more details 

        :return: The http_browser_color_depth of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._http_browser_color_depth

    @http_browser_color_depth.setter
    def http_browser_color_depth(self, http_browser_color_depth):
        """
        Sets the http_browser_color_depth of this Riskv1decisionsDeviceInformation.
        Value represents the bit depth of the color palette for displaying images, in bits per pixel. Example : 24, refer https://en.wikipedia.org/wiki/Color_depth for more details 

        :param http_browser_color_depth: The http_browser_color_depth of this Riskv1decisionsDeviceInformation.
        :type: str
        """
        if http_browser_color_depth is not None and len(http_browser_color_depth) > 2:
            raise ValueError("Invalid value for `http_browser_color_depth`, length must be less than or equal to `2`")

        self._http_browser_color_depth = http_browser_color_depth

    @property
    def http_browser_screen_height(self):
        """
        Gets the http_browser_screen_height of this Riskv1decisionsDeviceInformation.
        Total height of the Cardholder's scree in pixels, example: 864. 

        :return: The http_browser_screen_height of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._http_browser_screen_height

    @http_browser_screen_height.setter
    def http_browser_screen_height(self, http_browser_screen_height):
        """
        Sets the http_browser_screen_height of this Riskv1decisionsDeviceInformation.
        Total height of the Cardholder's scree in pixels, example: 864. 

        :param http_browser_screen_height: The http_browser_screen_height of this Riskv1decisionsDeviceInformation.
        :type: str
        """
        if http_browser_screen_height is not None and len(http_browser_screen_height) > 6:
            raise ValueError("Invalid value for `http_browser_screen_height`, length must be less than or equal to `6`")

        self._http_browser_screen_height = http_browser_screen_height

    @property
    def http_browser_screen_width(self):
        """
        Gets the http_browser_screen_width of this Riskv1decisionsDeviceInformation.
        Total width of the cardholder's screen in pixels. Example: 1536. 

        :return: The http_browser_screen_width of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._http_browser_screen_width

    @http_browser_screen_width.setter
    def http_browser_screen_width(self, http_browser_screen_width):
        """
        Sets the http_browser_screen_width of this Riskv1decisionsDeviceInformation.
        Total width of the cardholder's screen in pixels. Example: 1536. 

        :param http_browser_screen_width: The http_browser_screen_width of this Riskv1decisionsDeviceInformation.
        :type: str
        """
        if http_browser_screen_width is not None and len(http_browser_screen_width) > 6:
            raise ValueError("Invalid value for `http_browser_screen_width`, length must be less than or equal to `6`")

        self._http_browser_screen_width = http_browser_screen_width

    @property
    def http_browser_time_difference(self):
        """
        Gets the http_browser_time_difference of this Riskv1decisionsDeviceInformation.
        Time difference between UTC time and the cardholder browser local time, in minutes, Example:300 

        :return: The http_browser_time_difference of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._http_browser_time_difference

    @http_browser_time_difference.setter
    def http_browser_time_difference(self, http_browser_time_difference):
        """
        Sets the http_browser_time_difference of this Riskv1decisionsDeviceInformation.
        Time difference between UTC time and the cardholder browser local time, in minutes, Example:300 

        :param http_browser_time_difference: The http_browser_time_difference of this Riskv1decisionsDeviceInformation.
        :type: str
        """
        if http_browser_time_difference is not None and len(http_browser_time_difference) > 5:
            raise ValueError("Invalid value for `http_browser_time_difference`, length must be less than or equal to `5`")

        self._http_browser_time_difference = http_browser_time_difference

    @property
    def user_agent_browser_value(self):
        """
        Gets the user_agent_browser_value of this Riskv1decisionsDeviceInformation.
        Value of the User-Agent header sent by the customer’s web browser. Note If the customer’s browser provides a value, you must include it in your request. 

        :return: The user_agent_browser_value of this Riskv1decisionsDeviceInformation.
        :rtype: str
        """
        return self._user_agent_browser_value

    @user_agent_browser_value.setter
    def user_agent_browser_value(self, user_agent_browser_value):
        """
        Sets the user_agent_browser_value of this Riskv1decisionsDeviceInformation.
        Value of the User-Agent header sent by the customer’s web browser. Note If the customer’s browser provides a value, you must include it in your request. 

        :param user_agent_browser_value: The user_agent_browser_value of this Riskv1decisionsDeviceInformation.
        :type: str
        """
        if user_agent_browser_value is not None and len(user_agent_browser_value) > 255:
            raise ValueError("Invalid value for `user_agent_browser_value`, length must be less than or equal to `255`")

        self._user_agent_browser_value = user_agent_browser_value

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
        if not isinstance(other, Riskv1decisionsDeviceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
