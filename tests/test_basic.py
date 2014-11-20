from ppp_spell_checker import StringCorrector
import aspell

from unittest import TestCase

class DependenciesTreeTests(TestCase):

    def testTrueSentences(self):
        corrector = StringCorrector('en')
        original='Who is the president of the United States?'
        corrected=corrector.correctString(original)
        self.assertEqual(corrected,original)

    def testFalseSentences(self):
        corrector = StringCorrector('en')
        original='Who is the pesident of the Uinted Statse?'
        corrected=corrector.correctString(original)
        expected='Who is the president of the United States'
        self.assertEqual(corrected,expected)
