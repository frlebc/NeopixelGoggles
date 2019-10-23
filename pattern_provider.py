import random

from pattern_list import PatternsDict

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
            self.mColor = PatternsDict[patternKey]
    
PatternProviderInstance = PatternProvider()