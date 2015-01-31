"""Request handler of the module."""

import copy
import aspell
import re
from ppp_datamodel import Sentence, Resource
from ppp_datamodel.communication import TraceItem, Response
from ppp_libmodule.exceptions import ClientError

class Word:
    """
        A class to manipulate words.
    """
    def __init__(self,string,beginOffset):
        self.string = string
        self.corrected = False
        self.beginOffset = beginOffset

    def __str__(self):
        return "({0},{1},{2})".format(str(self.string),str(self.corrected),str(self.beginOffset))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def copy(self):
        return copy.deepcopy(self)

class StringCorrector:
    """
        A class to perform spell checking.
        A new instance of the object has to be created for each string.
    """
    quotationList = ['“','”','"']
    def __init__(self, language):
        self.numberCorrections = 0
        self.numberWords = 0
        self.speller = aspell.Speller('lang', language)
        self.quotations = set()

    def correct(self, w):
        """
            Take in input a word.
            Return the corrected word (unchanged if it was already correct).
        """
        if w.beginOffset in self.quotations:
            return w
        if self.speller.check(w.string):
            return w
        if w.string.isdecimal():
            return w
        else:
            self.numberCorrections += 1
            w.string = self.speller.suggest(w.string)[0]
            w.corrected = True
            return w

    def correctList(self, wordList):
        """
            Take in input a list of words.
            Return the list of correct words.
        """
        return [self.correct(w) for w in wordList]

    def tokenize(self,s):
        """
            Returns the list of the words in s.
        """
        wordList = re.findall(r"[\w']+", s)
        result = []
        wordId = 0
        for i in range(0,len(wordList)):
            newId = s.index(wordList[i])
            wordId += newId
            result.append(Word(wordList[i],wordId))
            wordId += len(wordList[i])
            s=s[newId+len(wordList[i]):]
        return result

    def quotationTraversal(self,s):
        """
            Fill the quotation set.
        """
        inquote=False
        for i in range(0,len(s)):
            if s[i] in self.quotationList:
                inquote = not inquote
            elif inquote:
                self.quotations.add(i)

    def correctString(self, s):
        """
            Return the corrected string.
        """
        wordList = self.tokenize(s)
        self.numberWords = len(wordList)
        self.quotationTraversal(s)
        correctedList = self.correctList([w.copy() for w in wordList])
        result = ""
        oldId = 0
        for i in range(0,len(correctedList)):
            result += s[oldId:correctedList[i].beginOffset]
            result += correctedList[i].string
            oldId = correctedList[i].beginOffset+len(wordList[i].string)
        result += s[oldId:len(s)]
        return result

class RequestHandler:
    def __init__(self, request):
        self.request = request

    def answer(self):
        if not isinstance(self.request.tree, Sentence):
            return []
        corrector = StringCorrector(self.request.language)
        result = corrector.correctString(self.request.tree.value)
        if corrector.numberCorrections == 0:
            return []
        outputTree = Sentence(result)
        relevance = self.request.measures.get('relevance', 0) + corrector.numberCorrections/corrector.numberWords
        meas = {'accuracy': 0.5, 'relevance': relevance}
        trace = self.request.trace + [TraceItem('spell-checker', outputTree, meas)]
        response = Response(language=self.request.language, tree=outputTree, measures=meas, trace=trace)
        return [response]
