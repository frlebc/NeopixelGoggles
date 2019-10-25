import os

def reboot():
    os.system("sudo reboot now")

def poweroff():
    os.system("sudo poweroff")

def rpiControl(value):
    if value == "poweroff":
        poweroff()
    elif value == "reboot":
        reboot()