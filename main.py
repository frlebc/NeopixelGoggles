import random
import board
import neopixel
import queue
import time

from blink_patterns.blink_pattern import BlinkPatternWithColor
from color_pattern_list import ColorPatterns
from neopixel_hardware import *
from remote.bt_connection import BtConnection
from remote.bt_protocol import BtProto

from color_provider import *
from pattern_provider import *

#TODO implement a clean signal handler
#signal.signal(signal.SIGINT, self.stopSignalHandler)
#signal.signal(signal.SIGTERM, self.stopSignalHandler)

#BtConnection() #This automatically starts the receiving thread

q = queue.Queue()
btConnection = BtConnection(q).start()
btProto = BtProto(q)


while True:
    btProto.read()
    if ColorProviderInstance.getLedOn() :
        pat = PatternProviderInstance.getPattern()
        pat.setColorPattern(ColorProviderInstance.getColor())
        pat.run()
    else:
        pixels.fill((0,0,0))
        pixels.show()
        time.sleep(0.25)