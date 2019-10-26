# pip install gpiozero
from gpiozero import CPUTemperature

def getCpuTemp():
    return CPUTemperature().temperature