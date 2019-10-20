from color_patterns.color_pattern import IColorPattern

class RedPattern(IColorPattern):
    def getColor(self, iter):
        return (255, 0, 0)

class GreenPattern(IColorPattern):
    def getColor(self, iter):
        return (0, 255, 0)

class BluePattern(IColorPattern):
    def getColor(self, iter):
        return (0, 0, 255)