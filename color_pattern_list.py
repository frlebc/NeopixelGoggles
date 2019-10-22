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