from blink_patterns.blink_pattern import IBlinkTimePattern

import random
import time

class StrobeRandomPattern(IBlinkTimePattern):
    cNbPixelsPerIteration = 2

    def __init__(self, pixels, pixelsIndex, time1, time2):
        self.mPixels = pixels
        self.mPixelsIndex = pixelsIndex
        self.mTimeOn = time1
        self.mTimeOff = time2

    def runIteration(self):
        for i in range(StrobeRandomPattern.cNbPixelsPerIteration):
            wIndex = self.mPixelsIndex[random.randint(0, len(self.mPixelsIndex)-1)]
            self.mPixels[wIndex] = (255, 255, 255)
        self.mPixels.show()
        time.sleep(self.mTimeOn)
        for i in self.mPixelsIndex:
            self.mPixels[i] = (0, 0, 0)
        self.mPixels.show()
        time.sleep(self.mTimeOff)

class StrobeBlinkPattern(IBlinkTimePattern):

    def __init__(self, pixels, pixelsIndex, time1, time2):
        self.mPixels = pixels
        self.mPixelsIndex = pixelsIndex
        self.mTimeOn = time1
        self.mTimeOff = time2

    def runIteration(self):
        for i in self.mPixelsIndex:
            self.mPixels[i] = (255, 255, 255)
        self.mPixels.show()
        time.sleep(self.mTimeOn)
        for i in self.mPixelsIndex:
            self.mPixels[i] = (0, 0, 0)
        self.mPixels.show()
        time.sleep(self.mTimeOff)