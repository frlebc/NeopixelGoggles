import abc

class IColorPattern(abc.ABC):
    # @abc.abstractmethod
    # def __init__(self, pixels, pixelsIndex, time1, time2):
    #     pass

    @abc.abstractmethod
    def getColor(self, iter):
        pass