from unittest import TestCase
from ppp_datamodel.communication import Request
from ppp_datamodel import Triple, Resource, Missing, Sentence
from ppp_libmodule.tests import PPPTestCase

from ppp_spell_checker import app

class RequestHandlerTest(PPPTestCase(app)):
    def testCorrectSentence(self):
        original = 'Who is the president of the United States'
        j = {'id': '1', 'language': 'en', 'measures': {}, 'trace': [],
             'tree': {'type': 'sentence', 'value': original}}
        answer = self.request(j)
        self.assertEqual(len(answer), 0, answer)

    def testWrongSentence(self):
        original = 'Who is the pesident of the United States'
        expected = 'Who is the president of the United States'
        j = {'id': '1', 'language': 'en', 'measures': {}, 'trace': [],
             'tree': {'type': 'sentence', 'value': original}}
        answer = self.request(j)
        self.assertEqual(len(answer), 1, answer)
        self.assertEqual(answer[0].tree, Sentence(value=expected))

    def testIrrelevantInput(self):
        original = 'Who is the president of the United States'
        j = {'id': '1', 'language': 'en', 'measures': {}, 'trace': [],
             'tree': {'type': 'resource', 'value': original}}
        answer = self.request(j)
        self.assertEqual(len(answer), 0, answer)
