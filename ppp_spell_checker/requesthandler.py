"""Request handler of the module."""

import aspell
import re

def correct(w,speller):
    """
        Take in input a word.
        Return the corrected word (unchanged if it was already correct).
    """
    if speller.check(w):
        return w
    else:
        return speller.suggest(w)[0]

def correctList(wordList,speller):
    """
        Take in input a list of words.
        Return the list of correct words.
    """
    return [correct(w,speller) for w in wordList]

def tokenize(s):
    """
        Returns the list of the words in s.
    """
    return re.findall(r"[\w']+", s)

def correctString(s,speller):
    wordList = tokenize(s)
    wordList = correctList(wordList,speller)
    return ' '.join(wordList)

from ppp_core.exceptions import ClientError

class RequestHandler:
    def __init__(self, request):
        self.request = request

    def answer(self):
        if not isinstance(self.request.tree, Sentence):
            return []
        speller = aspell.Speller('lang', 'en')
        result = correctString(self.request.tree.value,speller)
        outputTree=Resource(result, value_type='sentence')
        meas = {'accuracy': 0.5, 'relevance': 0.5}
        trace = self.request.trace + [TraceItem('spell-checker', outputTree, meas)]
        response = Response('en', outputTree, meas, trace)
        print(repr(outputTree))
        return [outputTree]
