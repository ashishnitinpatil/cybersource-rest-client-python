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
from CyberSource.apis.payment_instrument_api import PaymentInstrumentApi


class TestPaymentInstrumentApi(unittest.TestCase):
    """ PaymentInstrumentApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.payment_instrument_api.PaymentInstrumentApi()

    def tearDown(self):
        pass

    def test_delete_payment_instrument(self):
        """
        Test case for delete_payment_instrument

        Delete a Payment Instrument
        """
        pass

    def test_get_payment_instrument(self):
        """
        Test case for get_payment_instrument

        Retrieve a Payment Instrument
        """
        pass

    def test_patch_payment_instrument(self):
        """
        Test case for patch_payment_instrument

        Update a Payment Instrument
        """
        pass

    def test_post_payment_instrument(self):
        """
        Test case for post_payment_instrument

        Create a Payment Instrument
        """
        pass


if __name__ == '__main__':
    unittest.main()
