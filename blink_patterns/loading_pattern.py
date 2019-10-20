from blink_patterns.blink_pattern import IBlinkPattern

class LoadingPattern(IBlinkPattern):
    def __init__(self, pixels, pixelsIndex):
        self.mPixels = pixels
        self.mPixelsIndex = pixelsIndex
        self.mIterationCount = 0

    def runIteration(self):
        wIndex = self.mPixelsIndex[self.mIterationCount]
        self.mPixels[wIndex] = (255, 255, 255)
        self.mPixels.show()
        self.mIterationCount += 1