import random
import board
import neopixel
import queue

from blink_patterns.blink_pattern import BlinkPatternWithColor
from pattern_list import wPatterns, wPatternsTest #TODO remove wPatternsTest
from color_pattern_list import ColorPatterns
from neopixel_hardware import *
from remote.bt_connection import BtConnection
from remote.bt_protocol import BtProto

#TODO implement a clean signal handler
#signal.signal(signal.SIGINT, self.stopSignalHandler)
#signal.signal(signal.SIGTERM, self.stopSignalHandler)

#BtConnection() #This automatically starts the receiving thread

q = queue.Queue()
btConnection = BtConnection(q).start()
btProto = BtProto(q)


while True:
    random.shuffle(wPatterns)

    for wRunner in wPatterns:
        wRunner.setColorPattern(random.choice(ColorPatterns)) #TODO if wColor is a 2-eye pattern (ex: rainbow): apply on both, otherwise have a different for each ring

    for wRunner in wPatterns:
        wRunner.run()