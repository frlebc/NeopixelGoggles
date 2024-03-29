from color_patterns.rainbow_pattern import *
from color_patterns.solid_color_pattern import *
from color_patterns.alternate_colors import *

ColorPatterns = [
    WhitePattern(),
    RedPattern(),
    GreenPattern(),
    BluePattern(),
    YellowPattern(),
    MagentaPattern(),
    CyanPattern(),
    PurplePattern(),
    OrangePattern(),
    RainbowPattern(),
    RandomPattern(),
    AlternateColors([YELLOW, PURPLE]),
    AlternateColors([BLUE, WHITE]),
    AlternateColors([BLUE, RED]),
    AlternateColors([BLUE, WHITE, RED, WHITE]),
    AlternateColors([CYAN, GREEN]),
    AlternateColors([YELLOW, RED, ORANGE]),
    AlternateColors([MAGENTA, GREEN]),
    AlternateColors([ORANGE, GREEN]),
    AlternateColors([WHITE, RED]),
    AlternateColors([YELLOW, MAGENTA]),
    AlternateColors([BLUE, PURPLE, MAGENTA, CYAN]),
    AlternateColors([BLUE, MAGENTA]),
    AlternateColors([CYAN, PURPLE]),
    AlternateColors([CYAN, ORANGE]),
    AlternateColors([CYAN, PURPLE]),
]

ColorDict = {
    "white":WhitePattern(),
    "red":RedPattern(),
    "green":GreenPattern(),
    "blue":BluePattern(),
    "yellow":YellowPattern(),
    "magenta":MagentaPattern(),
    "cyan":CyanPattern(),
    "purple":PurplePattern(),
    "orange":OrangePattern(),
    "rainbow":RainbowPattern(),
    "random":RandomPattern(),
}