from blink_patterns.blink_pattern import BaseBlinkPattern
from neopixel_hardware import neopixelAllOff

import time

class BlinkPatternRunner:
    def __init__(self, blinkPatterns, nbRepeat):
        self.mPatterns = blinkPatterns
        self.mNbRepeat = nbRepeat

    def run(self):
        for i in range(0, self.mNbRepeat):
            for wPattern in self.mPatterns:
                wPattern.runIteration()
        #neopixelAllOff()

    def getPatterns(self):
        return self.mPatterns