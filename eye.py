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

    def loadingPatternUpper(self):
        for i in reversed(self.mPixelsIndex[8:16]): #todo should use num_pixels constant instead
            self.mPixels[i] = (255, 255, 255)
            self.mPixels.show()
            time.sleep(0.1)
