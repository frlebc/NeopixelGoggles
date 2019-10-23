import random

from color_pattern_list import ColorPatterns, ColorDict
from color_patterns.solid_color_pattern import RGBPattern

class ColorProvider:
    def __init__(self):
        self.mColor = random.choice(ColorPatterns)
        self.mRandom = True

    def getColor(self):
        if self.mRandom:
            return random.choice(ColorPatterns)
        return self.mColor

    def setColorPreset(self, colorKey):
        self.mRandom = (colorKey == "fullrandom")
        if colorKey in ColorDict:
            self.mColor = ColorDict[colorKey]
    
    def setColorRGB(self, rgbTuple):
        self.mColor = RGBPattern(rgbTuple)

ColorProviderInstance = ColorProvider()