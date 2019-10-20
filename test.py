import time
import board
import neopixel
import random

from eye import Eye
from blink_patterns.loading_pattern import LoadingPattern
 
 
# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin = board.D18
 
# On a Raspberry pi, use this instead, not all pins are supported
#pixel_pin = board.D18
 
# The number of NeoPixels
num_pixels = 32
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)
 
 
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)
 
 
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def strob_random(waitOff, waitOn):
    pixels[random.randint(0, num_pixels-1)] = (255, 255, 255)
    pixels[random.randint(0, num_pixels-1)] = (255, 255, 255)
    pixels.show()
    time.sleep(waitOn)
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(waitOff)

def strob_blink(waitOff, waitOn):
    pixels.fill((255, 255, 255))
    pixels.show()
    time.sleep(waitOn)
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(waitOff)

def loadingPattern(): 
    rightEye = Eye(pixels, 0, 4)
    leftEye = Eye(pixels, 16, 2)

    leftEye.setPattern(LoadingPattern(pixels, leftEye.getPixelsIndex()))
    rightEye.setPattern(LoadingPattern(pixels, rightEye.getPixelsIndex()))

    for i in range(16):
        leftEye.run()
        rightEye.run()
        time.sleep(0.1)

loadingPattern()

#while True:
    #rainbow_cycle(0.001)    # rainbow cycle with 1ms delay per step
    #strob_random(0.02, 0.0005)
    #strob_blink(0.07, 0.02)
