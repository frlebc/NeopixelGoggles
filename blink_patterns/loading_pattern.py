from blink_patterns.blink_pattern import BaseBlinkPattern, BlinkPatternWithColor
from blink_patterns.time_factor import TimeFactorInstance

class LoadingPattern(BaseBlinkPattern, BlinkPatternWithColor):
    cNbCyclesForPattern = 2

    def __init__(self, pixels, pixelsIndex, color, time):
        self.mPixels = pixels
        self.mPixelsIndex = pixelsIndex
        self.mIterationCount = 0
        self.mNbCycle = len(pixelsIndex) * self.cNbCyclesForPattern
        self.mColorPattern = color
        self.mTime = time

    def runIteration(self):
        wCycleIter = self.getCycleIter()
        if (self.mIterationCount // len(self.mPixelsIndex)) == 0:
            wIndex = self.mPixelsIndex[wCycleIter]
            self.mPixels[wIndex] = self.getColor(wCycleIter)
            self.mPixels.show()
        else:
            wIndex = self.mPixelsIndex[wCycleIter]
            self.mPixels[wIndex] = (0, 0, 0)
            self.mPixels.show()

        self.mIterationCount += 1
        self.mIterationCount %= self.mNbCycle

        TimeFactorInstance.sleep(self.mTime)

    def getCycleIter(self):
        return self.mIterationCount % len(self.mPixelsIndex)

    def getColor(self, cycleIter):
        wPixelIndex = (cycleIter * 256 // len(self.mPixelsIndex))
        return self.mColorPattern.getColor(wPixelIndex)

class LoadingPatternReverse(LoadingPattern):
    def getCycleIter(self):
        return (len(self.mPixelsIndex) - 1) - (self.mIterationCount % len(self.mPixelsIndex))

class LoadingPatternHalf(LoadingPattern):
    cNbCyclesForPattern = 1

class LoadingPatternHalfReverse(LoadingPatternReverse):
    cNbCyclesForPattern = 1

