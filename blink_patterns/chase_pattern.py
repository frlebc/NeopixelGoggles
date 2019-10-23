from blink_patterns.blink_pattern import BaseBlinkPattern, BlinkPatternWithColor
from blink_patterns.time_factor import TimeFactorInstance

class ChasePattern(BaseBlinkPattern, BlinkPatternWithColor):
    def __init__(self, pixels, pixelsIndex, color, nbPixelsSimultaneous, time):
        self.mPixels = pixels
        self.mPixelsIndex = pixelsIndex
        self.mIterationCount = 0
        self.mColorPattern = color
        self.mNbPixelsSimultaneous = nbPixelsSimultaneous
        self.mTime = time

    def runIteration(self):
        for wPixelIndex in self.mPixelsIndex:
            self.mPixels[wPixelIndex] = (0, 0, 0)

        for i in self.getPixelsToLight():
            wIndex = self.mPixelsIndex[i]
            self.mPixels[wIndex] = self.getColor(i)
        self.mPixels.show()

        self.mIterationCount += 1
        self.mIterationCount % len(self.mPixelsIndex)

        TimeFactorInstance.sleep(self.mTime)

    def getPixelsToLight(self):
        wIndices = []
        for i in range(0, self.mNbPixelsSimultaneous):
            wIndex = (i * len(self.mPixelsIndex)) // self.mNbPixelsSimultaneous
            wIndices.append((self.mIterationCount + wIndex) % len(self.mPixelsIndex))
        return wIndices

    def getColor(self, cycleIter):
        wPixelIndex = (cycleIter * 256 // len(self.mPixelsIndex))
        return self.mColorPattern.getColor(wPixelIndex)

class ChasePatternReverse(ChasePattern):
    def getPixelsToLight(self):
        wIndices = []
        for i in reversed(range(0, self.mNbPixelsSimultaneous)):
            wIndex = (i * len(self.mPixelsIndex)) // self.mNbPixelsSimultaneous
            wIndices.append((len(self.mPixelsIndex) - self.mIterationCount + wIndex) % len(self.mPixelsIndex))
        return wIndices
