from blink_patterns.blink_pattern import BaseBlinkPattern, BlinkPatternWithColor
from neopixel_hardware import neopixelAllOff

import time

class BlinkPatternRunner(BlinkPatternWithColor):
    def __init__(self, blinkPatterns, nbRepeat):
        self.mPatterns = blinkPatterns
        self.mNbRepeat = nbRepeat

    def run(self):
        for i in range(0, self.mNbRepeat):
            for wPattern in self.mPatterns:
                wPattern.runIteration()
        #neopixelAllOff()

    def setColorPattern(self, color):
        for wPattern in self.mPatterns:
            wPattern.setColorPattern(color)