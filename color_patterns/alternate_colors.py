from color_patterns.color_pattern import IColorPattern
from color_patterns.solid_color_pattern import *

class AlternateColors(IColorPattern):
    def __init__(self, colors):
        self.mCount = 0
        self.mColors = colors

    def getColor(self, iter):
        self.mCount += 1
        return self.mColors[self.mCount % len(self.mColors)]
