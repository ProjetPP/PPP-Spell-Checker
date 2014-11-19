from ppp_spell_checker import correctString
import aspell

from unittest import TestCase

class DependenciesTreeTests(TestCase):

    def testTrueSentences(self):
        speller = aspell.Speller('lang', 'en')
        original='Who is the president of the United States?'
        corrected=correctString(original,speller)
        expected='Who is the president of the United States'
        self.assertEqual(corrected,expected)

    def testFalseSentences(self):
        speller = aspell.Speller('lang', 'en')
        original='Who is the pesident of the Uinted Statse?'
        corrected=correctString(original,speller)
        expected='Who is the president of the United States'
        self.assertEqual(corrected,expected)
