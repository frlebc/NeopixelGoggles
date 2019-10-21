import time
import random
import board
import neopixel

from eye import Eye

pixel_pin = board.D18
 
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

def neopixelAllOff():
    pixels.fill((0, 0, 0))