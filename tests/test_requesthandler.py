from unittest import TestCase
from ppp_datamodel.communication import Request
from ppp_datamodel import Triple, Resource, Missing
from ppp_libmodule.tests import PPPTestCase

from ppp_spell_checker import app

class RequestHandlerTest(PPPTestCase(app)):
    def testCorrectSentence(self):
        original = 'What is the birth date of George Washington'
        j = {'id': '1', 'language': 'en', 'measures': {}, 'trace': [],
             'tree': {'type': 'sentence', 'value': original}}
        answer = self.request(j)
        self.assertEquals(len(answer), 0)

    def testWrongSentence(self):
        original = 'What is the bitrh date of George Washington'
        expected = 'What is the birth date of George Washington'
        j = {'id': '1', 'language': 'en', 'measures': {}, 'trace': [],
             'tree': {'type': 'sentence', 'value': original}}
        answer = self.request(j)
        self.assertEquals(len(answer), 1)
        self.assertIsInstance(answer[0].tree, Resource)
        result = answer[0].tree.__getattr__('value')
        self.assertEqual(result, expected)
