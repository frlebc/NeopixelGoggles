import time
import board
import neopixel

from eye import Eye
from blink_patterns.blink_pattern import *
from blink_patterns.loading_pattern import *
from blink_patterns.strobe_pattern import *
from color_patterns.rainbow_pattern import RainbowPattern
from color_patterns.solid_color_pattern import *
from color_patterns.random_pattern import *
 
 
# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin = board.D18
 
# On a Raspberry pi, use this instead, not all pins are supported
#pixel_pin = board.D18
 
# The number of NeoPixels
nbPixelsPerRing = 16
nbRings = 2
nbPixels = nbRings * nbPixelsPerRing
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(pixel_pin, nbPixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)


rightEye = Eye(pixels, 0, nbPixelsPerRing, 0) #4
leftEye = Eye(pixels, 16, nbPixelsPerRing, 14) #2

wPatterns = [
    #StrobeBlinkPattern(pixels, list(range(0, nbPixels)), 0.02, 0.07),
    #StrobeRandomPattern(pixels, list(range(0, nbPixels)), 0.0005, 0.02),
    #LoadingPattern(pixels, leftEye.getPixelsIndex()),
    #LoadingPattern(pixels, rightEye.getPixelsIndex()),
    LoadingPatternReverse(pixels, leftEye.getPixelsIndex(), RandomPattern()),
    LoadingPatternReverse(pixels, rightEye.getPixelsIndex(), RandomPattern()),
]


while True:
    #rainbow_cycle(0.001)    # rainbow cycle with 1ms delay per step

    for wPattern in wPatterns:
        wPattern.runIteration()
        if not issubclass(wPattern.__class__, IBlinkTimePattern):
            time.sleep(0.04)
