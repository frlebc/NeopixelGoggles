import random

from pattern_list import PatternsDict

from pattern_list import InfiniteDict

class PatternProvider:
    def __init__(self):
        self.mPattern = list(PatternsDict.values())[0]
        self.mRandom = True

    def getPattern(self):
        if self.mRandom:
            return random.choice(list(PatternsDict.values()))
        return self.mPattern

    def setPattern(self, patternKey):
        self.mRandom = (patternKey == "fullrandom")
        if patternKey in PatternsDict:
            self.mPattern = PatternsDict[patternKey]
    
PatternProviderInstance = PatternProvider()