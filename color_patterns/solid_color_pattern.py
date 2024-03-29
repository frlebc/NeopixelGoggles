from color_patterns.color_pattern import IColorPattern

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
PURPLE = (64, 0, 255)
ORANGE = (255, 64, 0)

class WhitePattern(IColorPattern):
    def getColor(self, iter):
        return self.applyIntensity(WHITE)

class RedPattern(IColorPattern):
    def getColor(self, iter):
        return self.applyIntensity(RED)

class GreenPattern(IColorPattern):
    def getColor(self, iter):
        return self.applyIntensity(GREEN)

class BluePattern(IColorPattern):
    def getColor(self, iter):
        return self.applyIntensity(BLUE)

class YellowPattern(IColorPattern):
    def getColor(self, iter):
        return self.applyIntensity(YELLOW)

class MagentaPattern(IColorPattern):
    def getColor(self, iter):
        return self.applyIntensity(MAGENTA)

class CyanPattern(IColorPattern):
    def getColor(self, iter):
        return self.applyIntensity(CYAN)

class PurplePattern(IColorPattern):
    def getColor(self, iter):
        return self.applyIntensity(PURPLE)

class OrangePattern(IColorPattern):
    def getColor(self, iter):
        return self.applyIntensity(ORANGE)

class RGBPattern(IColorPattern):
    def __init__(self, rgbTuple):
        self.mRGBTuple = rgbTuple
    def getColor(self, iter):
        return self.applyIntensity(self.mRGBTuple)