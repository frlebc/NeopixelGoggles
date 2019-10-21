from blink_patterns.blink_pattern_runner import BlinkPatternRunner
from blink_patterns.blink_pattern import *
from blink_patterns.loading_pattern import *
from blink_patterns.strobe_pattern import *
from blink_patterns.chase_pattern import *

from full_on_patterns.full_on_pattern import FullOnRainbowPattern

from color_patterns.rainbow_pattern import *
from color_patterns.solid_color_pattern import *

from neopixel_hardware import *


wPatterns = [
    # Strobe
    BlinkPatternRunner([
        StrobeBlinkPattern(pixels, list(range(0, nbPixels)), BluePattern(), 0.02, 0.07),
    ], 8),

    BlinkPatternRunner([
        StrobeBlinkPattern(pixels, list(range(0, nbPixels)), BluePattern(), 0.02, 0.07),
    ], 8),

    BlinkPatternRunner([
        StrobeRandomPattern(pixels, list(range(0, nbPixels)), RandomPattern(), 0.01, 0.01),
    ], 2* nbPixels),

    BlinkPatternRunner([
        StrobeRandomPattern(pixels, list(range(0, nbPixels)), RandomPattern(), 0.01, 0.01),
    ], nbPixels),

    BlinkPatternRunner([
        StrobeRandomPattern(pixels, list(range(0, nbPixels)), RandomPattern(), 0.01, 0.01),
    ], nbPixels),

    # Loading
    BlinkPatternRunner([
        LoadingPattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 0.03),
        LoadingPattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 0.03),
    ], nbPixels),

    BlinkPatternRunner([
        LoadingPattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 0.03),
        LoadingPattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 0.03),
    ], nbPixelsPerRing),

    BlinkPatternRunner([
        LoadingPatternReverse(pixels, leftEye.getPixelsIndex(), MagentaPattern(), 0.03),
        LoadingPatternReverse(pixels, rightEye.getPixelsIndex(), OrangePattern(), 0.03),
    ], nbPixels),

    BlinkPatternRunner([
        LoadingPattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 0.03),
        LoadingPatternReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 0.03),
    ], nbPixels),

    BlinkPatternRunner([
        LoadingPatternReverse(pixels, leftEye.getPixelsIndex(), MagentaPattern(), 0.03),
        LoadingPattern(pixels, rightEye.getPixelsIndex(), OrangePattern(), 0.03),
    ], nbPixels),

    BlinkPatternRunner([
        LoadingPatternHalf(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 0.03),
        LoadingPatternHalf(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 0.03),
    ], nbPixelsPerRing),

    BlinkPatternRunner([
        LoadingPatternHalfReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 0.03),
        LoadingPatternHalfReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 0.03),
    ], nbPixelsPerRing),

    BlinkPatternRunner([
        LoadingPatternHalf(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 0.03),
        LoadingPatternHalfReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 0.03),
    ], nbPixelsPerRing),

    BlinkPatternRunner([
        LoadingPatternHalfReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 0.03),
        LoadingPatternHalf(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 0.03),
    ], nbPixelsPerRing),

    # Chase
    BlinkPatternRunner([
        ChasePattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 1, 0.02),
        ChasePattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 1, 0.02)
    ], nbPixelsPerRing),

    BlinkPatternRunner([
        ChasePattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 2, 0.03),
        ChasePattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 2, 0.03)
    ], nbPixelsPerRing),

    BlinkPatternRunner([
        ChasePattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 4, 0.03),
        ChasePattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 4, 0.03)
    ], nbPixels),

    BlinkPatternRunner([
        ChasePatternReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 1, 0.02),
        ChasePatternReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 1, 0.02),
    ], nbPixelsPerRing),

    BlinkPatternRunner([
        ChasePatternReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 2, 0.03),
        ChasePatternReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 2, 0.03),
    ], nbPixelsPerRing),

    BlinkPatternRunner([
        ChasePatternReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 4, 0.03),
        ChasePatternReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 4, 0.03),
    ], nbPixels),

    BlinkPatternRunner([
        ChasePattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 1, 0.03),
        ChasePatternReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 1, 0.03)
    ], nbPixelsPerRing),

    BlinkPatternRunner([
        ChasePattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 2, 0.03),
        ChasePatternReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 2, 0.03)
    ], nbPixelsPerRing),

    BlinkPatternRunner([
        ChasePattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 4, 0.03),
        ChasePatternReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 4, 0.03)
    ], nbPixels),

    BlinkPatternRunner([
        ChasePatternReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 1, 0.02),
        ChasePattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 1, 0.02),
    ], nbPixelsPerRing),

    BlinkPatternRunner([
        ChasePatternReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 2, 0.03),
        ChasePattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 2, 0.03),
    ], nbPixelsPerRing),

    BlinkPatternRunner([
        ChasePatternReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 4, 0.03),
        ChasePattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 4, 0.03),
    ], nbPixels),

]

wPatternsTest = [
    BlinkPatternRunner([
        FullOnRainbowPattern(pixels, leftEye.getPixelsIndex(), 0.03),
        FullOnRainbowPattern(pixels, rightEye.getPixelsIndex(), 0.03),
    ], nbPixelsPerRing),
]