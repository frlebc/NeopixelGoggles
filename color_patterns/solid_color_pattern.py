from color_patterns.color_pattern import IColorPattern

class WhitePattern(IColorPattern):
    def getColor(self, iter):
        return (255, 255, 255)

class RedPattern(IColorPattern):
    def getColor(self, iter):
        return (255, 0, 0)

class GreenPattern(IColorPattern):
    def getColor(self, iter):
        return (0, 255, 0)

class BluePattern(IColorPattern):
    def getColor(self, iter):
        return (0, 0, 255)

class YellowPattern(IColorPattern):
    def getColor(self, iter):
        return (255, 255, 0)

class MagentaPattern(IColorPattern):
    def getColor(self, iter):
        return (255, 0, 255)

class CyanPattern(IColorPattern):
    def getColor(self, iter):
        return (0, 255, 255)

class PurplePattern(IColorPattern):
    def getColor(self, iter):
        return (64, 0, 255)

class OrangePattern(IColorPattern):
    def getColor(self, iter):
        return (255, 64, 0)