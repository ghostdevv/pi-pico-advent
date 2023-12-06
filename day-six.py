from neopixel import NeoPixel
from machine import Pin
import time


# Define the LED pin number (2) and number of LEDs (1)
GRBled = NeoPixel(Pin(0), 1)
GRBled2 = NeoPixel(Pin(1), 1)

# Define some GRB colour variables
white = 240, 140, 255  # White-ish!
red = 0, 255, 0
green = 255, 0, 0
blue = 0, 0, 255
yellow = 255, 175, 150
orange = 238, 223, 105
pink = 150, 150, 200
purple = 40, 100, 255
iceblue = 150, 25, 200
unicorn = 175, 150, 255
bogey = 215, 100, 0

# Define our colour list
colours = [
    white,
    red,
    green,
    blue,
    yellow,
    orange,
    pink,
    purple,
    iceblue,
    unicorn,
    bogey,
]

# GRBled.fill((white))
# GRBled.write()

while True:
    for colour in colours:
        GRBled.fill((colour))
        GRBled.write()
        GRBled2.fill((colour))
        GRBled2.write()
        time.sleep_ms(200)

# count = 0

# while True:
#     GRBled.fill((count, count, count))
#     GRBled.write()

#     count = 0 if count == 255 else count + 1
#     time.sleep_ms(200)
