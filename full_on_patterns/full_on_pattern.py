from blink_patterns.blink_pattern import BaseBlinkPattern, BlinkPatternWithColor
from blink_patterns.time_factor import TimeFactorInstance

from color_patterns.rainbow_pattern import RainbowPattern

class FullOnRainbowPattern(BaseBlinkPattern):
    def __init__(self, pixels, pixelsIndex, time):
        self.mPixels = pixels
        self.mPixelsIndex = pixelsIndex
        self.mTime = time
        self.mRainbow = RainbowPattern()
        self.mIterationCount = 0
        self.mNbCycle = len(pixelsIndex)

    def runIteration(self):
        wCycleIter = self.mIterationCount % len(self.mPixelsIndex)
        wColorIndex = wCycleIter * 256 // len(self.mPixelsIndex)
        for i in range(0, len(self.mPixelsIndex)):
            wIndex = self.mPixelsIndex[i]
            self.mPixels[wIndex] = self.mRainbow.getColor(wColorIndex)
        self.mPixels.show()
        TimeFactorInstance.sleep(self.mTime)

        self.mIterationCount += 1
        self.mIterationCount %= self.mNbCycle