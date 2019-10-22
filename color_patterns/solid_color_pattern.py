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
        return WHITE

class RedPattern(IColorPattern):
    def getColor(self, iter):
        return RED

class GreenPattern(IColorPattern):
    def getColor(self, iter):
        return GREEN

class BluePattern(IColorPattern):
    def getColor(self, iter):
        return BLUE

class YellowPattern(IColorPattern):
    def getColor(self, iter):
        return YELLOW

class MagentaPattern(IColorPattern):
    def getColor(self, iter):
        return MAGENTA

class CyanPattern(IColorPattern):
    def getColor(self, iter):
        return CYAN

class PurplePattern(IColorPattern):
    def getColor(self, iter):
        return PURPLE

class OrangePattern(IColorPattern):
    def getColor(self, iter):
        return ORANGE