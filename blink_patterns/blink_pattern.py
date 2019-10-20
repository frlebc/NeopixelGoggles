import abc

class IBlinkPattern(abc.ABC):
    @abc.abstractmethod
    def __init__(self, pixels, pixelsIndex):
        pass

    @abc.abstractmethod
    def runIteration(self):
        pass

class IBlinkTimePattern(IBlinkPattern):
    @abc.abstractclassmethod
    def __init__(self, pixels, pixelsIndex, time1, time2):
        pass