"""Request handler of the module."""

import aspell
import re
from ppp_datamodel import Sentence, Resource
from ppp_datamodel.communication import TraceItem, Response
from ppp_libmodule.exceptions import ClientError

class StringCorrector:
    """
        A class to perform spell checking.
    """
    def __init__(self, language):
        self.madeCorrection = False
        self.speller = aspell.Speller('lang', language)
    def correct(self,w):
        """
            Take in input a word.
            Return the corrected word (unchanged if it was already correct).
        """
        if self.speller.check(w):
            return w
        else:
            self.madeCorrection = True
            return self.speller.suggest(w)[0]
    def correctList(self,wordList):
        """
            Take in input a list of words.
            Return the list of correct words.
        """
        return [self.correct(w) for w in wordList]
    def tokenize(self,s):
        """
            Returns the list of the words in s.
        """
        return re.findall(r"[\w']+", s)
    def correctString(self,s):
        """
            Return the corrected string.
            If no correction were made, the string remains unchanged.
            Otherwise, punctuations marks might disapear.
        """
        wordList = self.tokenize(s)
        wordList = self.correctList(wordList)
        if self.madeCorrection:
            return ' '.join(wordList)
        return s

class RequestHandler:
    def __init__(self, request):
        self.request = request

    def answer(self):
        if not isinstance(self.request.tree, Sentence):
            return []
        corrector = StringCorrector(self.request.language)
        result = corrector.correctString(self.request.tree.value)
        if not corrector.madeCorrection:
            return []
        outputTree=Sentence(result)
        relevance = self.request.measures.get('relevance', 0) + 0.1
        meas = {'accuracy': 0.5, 'relevance': relevance}
        trace = self.request.trace + [TraceItem('spell-checker', outputTree, meas)]
        response = Response(language='en', tree=outputTree, measures=meas, trace=trace)
        print(repr(response))
        return [response]
