from blink_patterns.blink_pattern import BaseBlinkPattern, BlinkPatternWithColor
from blink_patterns.time_factor import TimeFactorInstance
from intensity_provider import IntensityProviderInstance

import random

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
            self.mPixels[wIndex] = IntensityProviderInstance.applyIntensity(self.mColorPattern.getColor(random.randint(0, 255)))
        self.mPixels.show()
        TimeFactorInstance.sleep(self.mTimeOn)
        for i in self.mPixelsIndex:
            self.mPixels[i] = (0, 0, 0)
        self.mPixels.show()
        TimeFactorInstance.sleep(self.mTimeOff)

    

class StrobeBlinkPattern(BaseBlinkPattern, BlinkPatternWithColor):

    def __init__(self, pixels, pixelsIndex, color, time1, time2):
        self.mPixels = pixels
        self.mPixelsIndex = pixelsIndex
        self.mColorPattern = color
        self.mTimeOn = time1
        self.mTimeOff = time2

    def runIteration(self):
        for i in self.mPixelsIndex:
            self.mPixels[i] = IntensityProviderInstance.applyIntensity(self.mColorPattern.getColor(i))
        self.mPixels.show()
        TimeFactorInstance.sleep(self.mTimeOn)
        for i in self.mPixelsIndex:
            self.mPixels[i] = (0, 0, 0)
        self.mPixels.show()
        TimeFactorInstance.sleep(self.mTimeOff)

class StrobeBlinkPausePattern(StrobeBlinkPattern):
    def __init__(self, pixels, pixelsIndex, color, time1, time2, time3):
        self.mIterationCount = 0
        self.mTimeSleep = time3
        super().__init__(pixels, pixelsIndex, color, time1, time2)

    def runIteration(self):
        self.mIterationCount += 1
        if (self.mIterationCount % 4) == 0:
            TimeFactorInstance.sleep(self.mTimeSleep)
        super().runIteration()

class StrobeLeftRightBlinkPattern(BaseBlinkPattern, BlinkPatternWithColor):

    def __init__(self, pixels, pixelsIndex, color, time1):
        self.mPixels = pixels
        self.mPixelsIndex = pixelsIndex
        self.mColorPattern = color
        self.mTimeOn = time1
        self.mIterationCount = 0

    def runIteration(self):
        self.mIterationCount += 1
        for i in self.mPixelsIndex:
            if self.mIterationCount % 2 == 0:
                if i < len(self.mPixelsIndex) / 2:
                    self.mPixels[i] = IntensityProviderInstance.applyIntensity(self.mColorPattern.getColor(i))
                else:
                    self.mPixels[i] = (0, 0, 0)
            else:
                if i < len(self.mPixelsIndex) / 2:
                    self.mPixels[i] = (0, 0, 0)
                else:
                    self.mPixels[i] = IntensityProviderInstance.applyIntensity(self.mColorPattern.getColor(i))
        self.mPixels.show()
        TimeFactorInstance.sleep(self.mTimeOn)
        