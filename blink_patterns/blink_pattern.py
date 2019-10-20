import abc

class IBlinkPattern(abc.ABC):
    @abc.abstractmethod
    def __init__(self, pixels, pixelsIndex):
        pass

    @abc.abstractmethod
    def runIteration(self):
        pass