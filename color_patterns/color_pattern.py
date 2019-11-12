import abc

from intensity_provider import IntensityProviderInstance

class IColorPattern(abc.ABC):
    @abc.abstractmethod
    def getColor(self, iter):
        pass

    def applyIntensity(self, color):
        return IntensityProviderInstance.applyIntensity(color)