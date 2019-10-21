import abc

class IColorPattern(abc.ABC):
    @abc.abstractmethod
    def getColor(self, iter):
        pass