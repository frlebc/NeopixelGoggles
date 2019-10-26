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
from cpu_temperature import getCpuTemp

from color_provider import *
from pattern_provider import *

def initSequence():
    for i in range(0,5):
        neopixelAllOnWhite()
        time.sleep(0.07)
        neopixelAllOff()
        time.sleep(0.12)

def main():
    #TODO implement a clean signal handler
    #signal.signal(signal.SIGINT, self.stopSignalHandler)
    #signal.signal(signal.SIGTERM, self.stopSignalHandler)

    #BtConnection() #This automatically starts the receiving thread

    q = queue.Queue()
    btConnection = BtConnection(q)
    btProto = BtProto(q, btConnection)

    btConnection.start()

    initSequence()

    iterCount = 0

    while True:
        btProto.read()
        if ColorProviderInstance.getLedOn() :
            pat = PatternProviderInstance.getPattern()
            pat.setColorPattern(ColorProviderInstance.getColor())
            pat.run()
        else:
            neopixelAllOff()
            time.sleep(0.25)

        if iterCount % 10 == 0:
            btProto.writeTemperature(getCpuTemp())
        iterCount += 1


main()