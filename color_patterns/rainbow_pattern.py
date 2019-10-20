from color_patterns.color_pattern import IColorPattern

import board
import neopixel

ORDER = neopixel.GRB
 
class RainbowPattern(IColorPattern):
    def getColor(self, iter):
        return self.wheel(iter & 255)

    def wheel(self, pos):
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
        return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0) #TODO abstract RGB order somewhere else to easily apply to all color patterns