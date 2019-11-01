from blink_patterns.blink_pattern_runner import BlinkPatternRunner
from blink_patterns.blink_pattern import *
from blink_patterns.loading_pattern import *
from blink_patterns.strobe_pattern import *
from blink_patterns.chase_pattern import *
from blink_patterns.infinite_pattern import *

from full_on_patterns.full_on_pattern import FullOnRainbowChasePattern, FullOnRainbowPattern #TODO create a list of preset pattern+color

from color_patterns.rainbow_pattern import *
from color_patterns.solid_color_pattern import *

from neopixel_hardware import *

StrobeDict = {
    "strobe.full":BlinkPatternRunner([
        StrobeBlinkPattern(pixels, list(range(0, nbPixels)), BluePattern(), 0.02, 0.07),
    ], 8),

    "strobe.pause":BlinkPatternRunner([
        StrobeBlinkPausePattern(pixels, list(range(0, nbPixels)), BluePattern(), 0.02, 0.07, 1),
    ], 8),

    "strobe.leftright":BlinkPatternRunner([
        StrobeLeftRightBlinkPattern(pixels, list(range(0, nbPixels)), RandomPattern(), 0.2),
    ], 4),

    "strobe.leftright.slow":BlinkPatternRunner([
        StrobeLeftRightBlinkPattern(pixels, list(range(0, nbPixels)), RandomPattern(), 0.5),
    ], 4),
}

StrobeRandomDict = {
    "strobe.random.long":BlinkPatternRunner([
        StrobeRandomPattern(pixels, list(range(0, nbPixels)), RandomPattern(), 0.01, 0.01),
    ], 2 * nbPixels),

    "strobe.random":BlinkPatternRunner([
        StrobeRandomPattern(pixels, list(range(0, nbPixels)), RandomPattern(), 0.01, 0.01),
    ], nbPixels),
}

LoadingDict = {
        "load.full":BlinkPatternRunner([
        LoadingPattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 0.03),
        LoadingPattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 0.03),
    ], nbPixels),

    "load.full.reverse":BlinkPatternRunner([
        LoadingPatternReverse(pixels, leftEye.getPixelsIndex(), MagentaPattern(), 0.03),
        LoadingPatternReverse(pixels, rightEye.getPixelsIndex(), OrangePattern(), 0.03),
    ], nbPixels),

    "load.full.opposite":BlinkPatternRunner([
        LoadingPattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 0.03),
        LoadingPatternReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 0.03),
    ], nbPixels),

    "load.full.opposite.reverse":BlinkPatternRunner([
        LoadingPatternReverse(pixels, leftEye.getPixelsIndex(), MagentaPattern(), 0.03),
        LoadingPattern(pixels, rightEye.getPixelsIndex(), OrangePattern(), 0.03),
    ], nbPixels),

    "load.half":BlinkPatternRunner([
        LoadingPatternHalf(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 0.03),
        LoadingPatternHalf(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 0.03),
    ], nbPixelsPerRing),

    "load.half.reverse":BlinkPatternRunner([
        LoadingPatternHalfReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 0.03),
        LoadingPatternHalfReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 0.03),
    ], nbPixelsPerRing),

    "load.half.opposite":BlinkPatternRunner([
        LoadingPatternHalf(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 0.03),
        LoadingPatternHalfReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 0.03),
    ], nbPixelsPerRing),

    "load.half.opposite.reverse":BlinkPatternRunner([
        LoadingPatternHalfReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 0.03),
        LoadingPatternHalf(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 0.03),
    ], nbPixelsPerRing),
}

ChaseDict = {
    "chase.1":BlinkPatternRunner([
        ChasePattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 1, 0.02),
        ChasePattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 1, 0.02)
    ], nbPixels),

    "chase.2":BlinkPatternRunner([
        ChasePattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 2, 0.03),
        ChasePattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 2, 0.03)
    ], nbPixels),

    "chase.4":BlinkPatternRunner([
        ChasePattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 4, 0.03),
        ChasePattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 4, 0.03)
    ], nbPixels),

    "chase.8":BlinkPatternRunner([
        ChasePattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 8, 0.05),
        ChasePattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 8, 0.05)
    ], nbPixels),

    "chase.1.reverse":BlinkPatternRunner([
        ChasePatternReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 1, 0.02),
        ChasePatternReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 1, 0.02),
    ], nbPixels),

    "chase.2.reverse":BlinkPatternRunner([
        ChasePatternReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 2, 0.03),
        ChasePatternReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 2, 0.03),
    ], nbPixels),

    "chase.4.reverse":BlinkPatternRunner([
        ChasePatternReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 4, 0.03),
        ChasePatternReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 4, 0.03),
    ], nbPixels),

    "chase.8.reverse":BlinkPatternRunner([
        ChasePatternReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 8, 0.05),
        ChasePatternReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 8, 0.05),
    ], nbPixels),

    "chase.1.opposite":BlinkPatternRunner([
        ChasePattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 1, 0.03),
        ChasePatternReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 1, 0.03)
    ], nbPixels),

    "chase.2.opposite":BlinkPatternRunner([
        ChasePattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 2, 0.03),
        ChasePatternReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 2, 0.03)
    ], nbPixels),

    "chase.4.opposite":BlinkPatternRunner([
        ChasePattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 4, 0.03),
        ChasePatternReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 4, 0.03)
    ], nbPixels),

    "chase.8.opposite":BlinkPatternRunner([
        ChasePattern(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 8, 0.05),
        ChasePatternReverse(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 8, 0.05)
    ], nbPixels),

    "chase.1.opposite.reverse":BlinkPatternRunner([
        ChasePatternReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 1, 0.02),
        ChasePattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 1, 0.02),
    ], nbPixelsPerRing),

    "chase.2.opposite.reverse":BlinkPatternRunner([
        ChasePatternReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 2, 0.03),
        ChasePattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 2, 0.03),
    ], nbPixelsPerRing),

    "chase.4.opposite.reverse":BlinkPatternRunner([
        ChasePatternReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 4, 0.03),
        ChasePattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 4, 0.03),
    ], nbPixels),

    "chase.8.opposite.reverse":BlinkPatternRunner([
        ChasePatternReverse(pixels, leftEye.getPixelsIndex(), RainbowPattern(), 8, 0.05),
        ChasePattern(pixels, rightEye.getPixelsIndex(), RainbowPattern(), 8, 0.05),
    ], nbPixels),
}

FullOnDict = {
    "fullon.rainbow.allsame":BlinkPatternRunner([
        FullOnRainbowPattern(pixels, list(range(0, nbPixels)), 0.1),
    ], nbPixels),

    "fullon.rainbow.chase":BlinkPatternRunner([
        FullOnRainbowChasePattern(pixels, list(range(0, nbPixels)), 0.08),
    ], nbPixels),
}

InfiniteDict = {
    "infinite":BlinkPatternRunner([
        InfinitePattern(pixels, list(range(0, nbPixels)), 0.05),
    ], 58),
}

PatternsDict = {**StrobeRandomDict, **LoadingDict, **ChaseDict, **FullOnDict, **InfiniteDict}