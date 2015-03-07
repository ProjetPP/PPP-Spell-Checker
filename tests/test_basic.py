from unittest import TestCase
import itertools

from ppp_spell_checker import StringCorrector, Word
import aspell

class DependenciesTreeTests(TestCase):

    def testBasicWordMethods(self):
        a=Word("foo",2)
        b=Word("foo",2)
        self.assertEqual(a, b)
        self.assertEqual(str(a), str(b))

    def testTokenization(self):
        corrector = StringCorrector('en')
        s = 'this is * ~ a ## word list "for test purpose" '
        tokens = corrector.tokenize(s)
        self.assertEqual([w.string for w in tokens],['this','is','a','word','list','for','test','purpose'])
        for w in tokens:
            self.assertEqual(w.string, s[w.beginOffset:w.beginOffset+len(w.string)])

    def testNumber(self):
        corrector = StringCorrector('en')
        original = '42 92.123 1*2*42+3.7'
        corrected=corrector.correctString(original)
        self.assertEqual(original, corrected)
        self.assertEqual(corrector.numberCorrections,0)

    def testTrueSentences(self):
        corrector = StringCorrector('en')
        original='Who is the president of the United States?'
        corrected=corrector.correctString(original)
        self.assertEqual(corrected, original)
        self.assertEqual(corrector.numberCorrections,0)

    def testFalseSentences(self):
        corrector = StringCorrector('en')
        original='Who is the pesident of the Uinted Statse?'
        corrected=corrector.correctString(original)
        expected='Who is the president of the United States?'
        self.assertEqual(corrected, expected)
        self.assertEqual(corrector.numberCorrections,3)

    def testPunctuation(self):
        corrector = StringCorrector('en')
        original=' * Who,. is! the : : pesident of the --- --- --- Uinted Statse? . ! '
        corrected=corrector.correctString(original)
        expected=' * Who,. is! the : : president of the --- --- --- United States? . ! '
        self.assertEqual(corrected, expected)

    def testTrueSentencesQuotation(self):
        for quotes in itertools.permutations(
                [('"', '"'), ("'", "'"), ('“', '”'), ('‘', '’'), ('«', '»')], 2):
            corrector = StringCorrector('en')
            original='Who %sis the%s president of the %sUnited States%s?' % (
                quotes[0][0], quotes[0][1], quotes[1][0], quotes[1][1]
            )
            corrected = corrector.correctString(original)
            self.assertEqual(corrected, original)
            self.assertEqual(corrector.numberCorrections,0)

    def testFalseSentencesQuotation(self):
        for quotes in itertools.permutations(
                [('"', '"'), ("'", "'"), ('“', '”'), ('‘', '’'), ('«', '»')], 2):
            corrector = StringCorrector('en')
            original='Who %sis the%s pesident of the %sUinted Statse%s?' % (
                quotes[0][0], quotes[0][1], quotes[1][0], quotes[1][1]
            )
            corrected = corrector.correctString(original)
            expected = original.replace('pesident', 'president')
            self.assertEqual(corrected, expected)
            self.assertEqual(corrector.numberCorrections, 1)

    def testPunctuationQuotation(self):
        corrector = StringCorrector('en')
        original=' * Who,. “is! the ”: : pesident “of” the ‘---’ --- --"- Uinted Statse? ." ! '
        corrected=corrector.correctString(original)
        expected=' * Who,. “is! the ”: : president “of” the ‘---’ --- --"- Uinted Statse? ." ! '
        self.assertEqual(corrected, expected)
