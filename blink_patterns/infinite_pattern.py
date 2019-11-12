from blink_patterns.blink_pattern import BaseBlinkPattern, BlinkPatternWithColor
from blink_patterns.time_factor import TimeFactorInstance
from intensity_provider import IntensityProviderInstance

class InfinitePattern(BaseBlinkPattern, BlinkPatternWithColor):
    def __init__(self, pixels, pixelsIndex, time):
        self.mPixels = pixels
        self.mPixelsIndex = pixelsIndex
        self.mIterationCount = 0
        self.mTime = time

    def runIteration(self):
        seq = [0,1,2,3,4,5,6,7,8,9,10,11,16,31,30,29,28,27,26,25,24,23,22,21,20,19,13,14,15]
        for wPixelIndex in self.mPixelsIndex:
            self.mPixels[wPixelIndex] = (0, 0, 0)

        i = seq[self.mIterationCount]
        self.mPixels[i] = self.mColorPattern.getColor(i)
        self.mPixels.show()

        self.mIterationCount += 1
        self.mIterationCount = (self.mIterationCount % len(seq))

        TimeFactorInstance.sleep(self.mTime)
        

    def getColor(self, cycleIter):
        wPixelIndex = (cycleIter * 256 // len(self.mPixelsIndex))
        return self.mColorPattern.getColor(wPixelIndex)

class InfinitePatternReverse(InfinitePattern):
    def getPixelsToLight(self):
        wIndices = []
        for i in reversed(range(0, self.mNbPixelsSimultaneous)):
            wIndex = (i * len(self.mPixelsIndex)) // self.mNbPixelsSimultaneous
            wIndices.append((len(self.mPixelsIndex) - self.mIterationCount + wIndex) % len(self.mPixelsIndex))
        return wIndices
