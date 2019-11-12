from color_provider import ColorProviderInstance
from pattern_provider import PatternProviderInstance
from blink_patterns.time_factor import TimeFactorInstance
from intensity_provider import IntensityProviderInstance
from rpi_control import rpiControl

def BtHandlerLed(value):
    ColorProviderInstance.setLedOn(value != "off")

def BtHandlerColorPreset(value):
    ColorProviderInstance.setColorPreset(value)

def BtHandlerRGB(value):
    rgbStrList = value.split(' ')
    if len(rgbStrList) == 3:
        rgbTuple = tuple(int(i) for i in rgbStrList)
        ColorProviderInstance.setColorRGB(rgbTuple)

def BtHandlerPatternPreset(value):
    PatternProviderInstance.setPattern(value)

def BtHandlerPattern(value):
    pass

def BtHandlerSpeed(value):
    TimeFactorInstance.setFactor(float(value))

def BtHandlerIntensity(value):
    IntensityProviderInstance.setLedIntensity(float(value))

def BtHandlerRpiControl(value):
    rpiControl(value)

BtProtocolHandlers = {
    "led":BtHandlerLed,
    "col":BtHandlerColorPreset,
    "rgb":BtHandlerRGB,
    "pat":BtHandlerPatternPreset,
    "p":BtHandlerPattern,
    "speed":BtHandlerSpeed,
    "int":BtHandlerIntensity,
    "rpi":BtHandlerRpiControl,
}