# NeopixelGoggles

I stumbled upon [this project](https://learn.adafruit.com/kaleidoscope-eyes-neopixel-led-goggles-trinket-gemma) on Adafruit. With Halloween coming soon, I decided to give it a try and create my own goggles. For my project, I replaced the small microcontroller by a Raspberry Pi Zero to easily control the pixels from my phone via Bluetooth!

This repo contains the Python software that runs on the Pi. It uses the [NeoPixel library](https://learn.adafruit.com/adafruit-neopixel-uberguide/python-circuitpython#python-installation-of-neopixel-library-17-9) and pybluez library.

## Running the code on the Pi Zero W
1. Install the [NeoPixel library](https://learn.adafruit.com/adafruit-neopixel-uberguide/python-circuitpython#python-installation-of-neopixel-library-17-9)
1. Install the pybluez library (apt-get install libbluetooth-dev && pip install pybluez)
1. Configure the `pixel_pin` in neopixel_hardware.py to match your setup
1. Upload the code to the Pi
1. Execute: `sudo python3 main.py` (sudo required by the NeoPixel lib to access hardware)
1. The pixels should blink 5 times at initialization then remain off until a bluetooth command is received

## Controlling the leds
The leds can be controlled via a simple ASCII based protocol over Bluetooth. There are many tutorials online to enable Bluetooth communication on the Pi Zero W. I created a this simple [android app](https://github.com/frlebc/LedControlApp) to change the patterns and colors.

## Hardware assembly
Everything is hidden inside the top hat, in which I made a small hole to pass the wires to the pixels. For the power, I used a small portable USB power bank. The power consumption is fairly low so I didn't care too much for the battery capacity. The size and weight were more important as I wanted to wear it on my head for many hours.

The Pi is powered via its USB port connected to the power bank. The pixels are powered through one of the Pi's 5V pin.

## Material
- [NeoPixel rings 16x](https://www.adafruit.com/product/1463)
- Raspberry Pi Zero W
- Small portable USB power bank (any cheap one will do, power consumption is fairly low)
- Soldering iron
- Jumper wires and connectors
- A top hat to hide the Pi and battery
- Some cool goggles!
