import abc

class BaseBlinkPattern(abc.ABC):
    @abc.abstractclassmethod
    def runIteration(self):
        pass

class BlinkPatternWithColor:
    def setColorPattern(self, color):
        self.mColorPattern = color