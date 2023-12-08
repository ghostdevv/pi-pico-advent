from utils import CounterSimple
from neopixel import NeoPixel
from machine import Pin, ADC
import time

potentiometer = ADC(Pin(26))
RGBled = NeoPixel(Pin(0), 12)

counter = CounterSimple(
    [
        Pin(10, Pin.OUT),
        Pin(11, Pin.OUT),
        Pin(12, Pin.OUT),
        Pin(13, Pin.OUT),
        Pin(14, Pin.OUT),
    ]
)

while True:
    # Place the reading on a scale of 0.0 - 1.0
    value = round(potentiometer.read_u16() / 65535, 1)

    value_five = int(round((value / 2) * 10, 1))

    # Set counter on scale of 1 - 5
    counter.set(value_five)

    values = {
        0: (0, 0, 0),
        1: (255, 0, 0),
        2: (0, 255, 0),
        3: (0, 0, 255),
        4: (255, 255, 255),
        5: (33, 96, 236),
    }

    RGBled.fill(values[value_five])
    RGBled.write()

    time.sleep_ms(50)
