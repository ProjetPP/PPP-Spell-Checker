from ppp_spell_checker import StringCorrector, Word
import aspell

from unittest import TestCase

class DependenciesTreeTests(TestCase):

    def testBasicWordMethods(self):
        a=Word("foo",2)
        b=Word("foo",2)
        self.assertEqual(a,b)
        self.assertEqual(str(a),str(b))

    def testTokenization(self):
        corrector = StringCorrector('en')
        s = 'this is * ~ a ## word list "for test purpose" '
        tokens = corrector.tokenize(s)
        self.assertEqual([w.string for w in tokens],['this','is','a','word','list','for','test','purpose'])
        for w in tokens:
            self.assertEqual(w.string,s[w.beginOffset:w.beginOffset+len(w.string)])

    def testTrueSentences(self):
        corrector = StringCorrector('en')
        original='Who is the president of the United States?'
        corrected=corrector.correctString(original)
        self.assertEqual(corrected,original)
        self.assertEqual(corrector.numberCorrections,0)

    def testFalseSentences(self):
        corrector = StringCorrector('en')
        original='Who is the pesident of the Uinted Statse?'
        corrected=corrector.correctString(original)
        expected='Who is the president of the United States?'
        self.assertEqual(corrected,expected)
        self.assertEqual(corrector.numberCorrections,3)

    def testPunctuation(self):
        corrector = StringCorrector('en')
        original=' * Who,. is! the : : pesident of the --- --- --- Uinted Statse? . ! '
        corrected=corrector.correctString(original)
        expected=' * Who,. is! the : : president of the --- --- --- United States? . ! '
        self.assertEqual(corrected,expected)


    def testTrueSentences(self):
        corrector = StringCorrector('en')
        original='Who "is the" president of the "United States"?'
        corrected=corrector.correctString(original)
        self.assertEqual(corrected,original)
        self.assertEqual(corrector.numberCorrections,0)

    def testFalseSentencesQuotation(self):
        corrector = StringCorrector('en')
        original='Who "is the" pesident of the "Uinted Statse"?'
        corrected=corrector.correctString(original)
        expected='Who "is the" president of the "Uinted Statse"?'
        self.assertEqual(corrected,expected)
        self.assertEqual(corrector.numberCorrections,1)

    def testPunctuation(self):
        corrector = StringCorrector('en')
        original=' * Who,. "is! the ": : pesident of the --- --- --"- Uinted Statse? ." ! '
        corrected=corrector.correctString(original)
        expected=' * Who,. "is! the ": : president of the --- --- --"- Uinted Statse? ." ! '
        self.assertEqual(corrected,expected)
