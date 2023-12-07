from utils import CounterSimple
from neopixel import NeoPixel
from machine import Pin, ADC
from random import randint
import time

potentiometer = ADC(Pin(26))
GRBled = NeoPixel(Pin(0), 1)

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

    # Set counter on scale of 1 - 5
    counter.set(int(round((value / 2) * 10, 1)))

    rand_max = int(value * 255)

    g = randint(0, rand_max)
    r = randint(0, rand_max)
    b = randint(0, rand_max)

    GRBled.fill((g, r, b))
    GRBled.write()

    print(
        f"Value is {value}, counter is {counter.count}, rand_max is {rand_max} ({g}, {r}, {b})"
    )

    time.sleep_ms(50)
