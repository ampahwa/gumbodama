
from unittest import TestCase, skip 

import API.endpoints as ep
from flask_restx import Resource, Api


class EndpointTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello(self):
        hello = ep.HelloWorld(Resource)
        ret = hello.get()
        self.assertIsInstance(ret, dict)

    def test_get_soup1(self):
        """
        Post-condition 1: return is a dictionary.
        """
        lr = ep.OSoup(Resource)
        ret = lr.get()
        self.assertIsInstance(ret, dict)
