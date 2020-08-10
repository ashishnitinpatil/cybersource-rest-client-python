# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import CyberSource
from CyberSource.rest import ApiException
from CyberSource.apis.customer_shipping_address_api import CustomerShippingAddressApi


class TestCustomerShippingAddressApi(unittest.TestCase):
    """ CustomerShippingAddressApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.customer_shipping_address_api.CustomerShippingAddressApi()

    def tearDown(self):
        pass

    def test_delete_customer_shipping_address(self):
        """
        Test case for delete_customer_shipping_address

        Delete a Customer Shipping Address
        """
        pass

    def test_get_customer_shipping_address(self):
        """
        Test case for get_customer_shipping_address

        Retrieve a Customer Shipping Address
        """
        pass

    def test_get_customer_shipping_addresses_list(self):
        """
        Test case for get_customer_shipping_addresses_list

        List Shipping Addresses for a Customer
        """
        pass

    def test_patch_customers_shipping_address(self):
        """
        Test case for patch_customers_shipping_address

        Update a Customer Shipping Address
        """
        pass

    def test_post_customer_shipping_address(self):
        """
        Test case for post_customer_shipping_address

        Create a Customer Shipping Address
        """
        pass


if __name__ == '__main__':
    unittest.main()
