from color_patterns.color_pattern import IColorPattern

import random

class RandomPattern(IColorPattern):
    def getColor(self, iter):
        wRed = random.choice([0,  128,  255])
        wGreen = random.choice([0,  128,  255])
        wBlue = random.choice([0,  128,  255])
        while wRed + wGreen + wBlue < 100:
            wRed = random.choice([0,  128,  255])
            wGreen = random.choice([0,  128,  255])
            wBlue = random.choice([0,  128,  255])
        return (wRed, wGreen, wBlue)