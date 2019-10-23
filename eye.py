import board
import neopixel
import time

from enum import Enum

class Eye:
    def __init__(self, pixels, baseAddr, nbPixels, zeroOffset):
        self.mPixels = pixels
        self.mPixelsIndex = list(range(baseAddr + zeroOffset,baseAddr + nbPixels)) + list(range(baseAddr, baseAddr + zeroOffset))
    
    def getPixelsIndex(self):
        return self.mPixelsIndex

    def setPattern(self, pattern):
        self.mPattern = pattern

    def run(self):
        self.mPattern.runIteration()
