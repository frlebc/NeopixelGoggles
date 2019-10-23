from color_provider import ColorProviderInstance

def BtHandlerColorPreset(value):
    ColorProviderInstance.setColorPreset(value)

def BtHandlerRGB(value):
    rgbStrList = value.split(' ')
    if len(rgbStrList) == 3:
        rgbTuple = tuple(int(i) for i in rgbStrList)
        ColorProviderInstance.setColorRGB(rgbTuple)

def BtHandlerPatternPreset(value):
    print("PatternPreset: ", value)

def BtHandlerPattern(value):
    print("Pattern: ", value)

BtProtocolHandlers = {
    "cp":BtHandlerColorPreset,
    "rgb":BtHandlerRGB,
    "pl":BtHandlerPatternPreset,
    "p":BtHandlerPattern,
}