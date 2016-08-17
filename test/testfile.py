import json
from __init__ import create_app
from flask import url_for
import unittest



class testClass1(unittest.TestCase):


    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()



    def tearDown(self):
        self.app_context.pop()


    def test_abc(self):
        res = self.client.get(url_for('app_v1.test'))
        response = json.loads(res.data)
        print(response)