from neopixel_hardware import neopixelAllOff

import os

def reboot():
    os.system("sudo reboot now")

def poweroff():
    os.system("sudo poweroff")

def rpiControl(value):
    if value == "poweroff":
        neopixelAllOff()
        poweroff()
    elif value == "reboot":
        neopixelAllOff()
        reboot()