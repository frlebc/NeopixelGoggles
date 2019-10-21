from blink_patterns.blink_pattern import BaseBlinkPattern, BlinkPatternWithColor

import random
import time

class StrobeRandomPattern(BaseBlinkPattern, BlinkPatternWithColor):
    cNbPixelsPerIteration = 2

    def __init__(self, pixels, pixelsIndex, color, time1, time2):
        self.mPixels = pixels
        self.mPixelsIndex = pixelsIndex
        self.mColorPattern = color
        self.mTimeOn = time1
        self.mTimeOff = time2

    def runIteration(self):
        for i in range(StrobeRandomPattern.cNbPixelsPerIteration):
            wIndex = self.mPixelsIndex[random.randint(0, len(self.mPixelsIndex)-1)]
            self.mPixels[wIndex] =  self.mColorPattern.getColor(random.randint(0, 255))
        self.mPixels.show()
        time.sleep(self.mTimeOn)
        for i in self.mPixelsIndex:
            self.mPixels[i] = (0, 0, 0)
        self.mPixels.show()
        time.sleep(self.mTimeOff)

    

class StrobeBlinkPattern(BaseBlinkPattern, BlinkPatternWithColor):

    def __init__(self, pixels, pixelsIndex, color, time1, time2):
        self.mPixels = pixels
        self.mPixelsIndex = pixelsIndex
        self.mColorPattern = color
        self.mTimeOn = time1
        self.mTimeOff = time2

    def runIteration(self):
        for i in self.mPixelsIndex:
            self.mPixels[i] = self.mColorPattern.getColor(i)
        self.mPixels.show()
        time.sleep(self.mTimeOn)
        for i in self.mPixelsIndex:
            self.mPixels[i] = (0, 0, 0)
        self.mPixels.show()
        time.sleep(self.mTimeOff)