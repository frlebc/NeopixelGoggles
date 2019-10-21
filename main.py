import time
import random
import board
import neopixel

from blink_patterns.blink_pattern import BlinkPatternWithColor
from pattern_list import wPatterns, wPatternsTest #TODO remove wPatternsTest
from color_pattern_list import ColorPatterns
from neopixel_hardware import *

while True:
    random.shuffle(wPatterns)

    for wRunner in wPatterns:
        wColor = random.choice(ColorPatterns) #TODO if wColor is a 2-eye pattern (ex: rainbow): apply on both, otherwise have a different for each ring
        for wPattern in wRunner.getPatterns():
            if wPattern is BlinkPatternWithColor:
                wPattern.setColorPattern(wColor)

    for wRunner in wPatterns:
        wRunner.run()