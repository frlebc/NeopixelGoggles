class IntensityProvider:
    def __init__(self):
        self.mIntensity = 0.15

    def setLedIntensity(self, int):
        self.mIntensity = int

    def applyIntensity(self, color):
        return tuple(int(self.mIntensity * x) for x in color)

IntensityProviderInstance = IntensityProvider()