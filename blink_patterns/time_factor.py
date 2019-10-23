import time

class TimeFactor:
    def __init__(self):
        self.mFactor = 1.0
        
    def sleep(self, duration):
        time.sleep(duration * 1 / self.mFactor)

    def setFactor(self, factor):
        self.mFactor = factor

TimeFactorInstance = TimeFactor()