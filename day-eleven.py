from neopixel import NeoPixel
from utils import debounce
from machine import Pin
import time

button_one = Pin(2, Pin.IN, Pin.PULL_DOWN)
button_two = Pin(3, Pin.IN, Pin.PULL_DOWN)
button_three = Pin(4, Pin.IN, Pin.PULL_DOWN)
button_four = Pin(5, Pin.IN, Pin.PULL_DOWN)

RGBled = NeoPixel(Pin(0), 15)

r = 0
g = 0
b = 0


def calc_c(val: int):
    new = int(val + (255 / 10))
    return new if new <= 255 else 0


def set_r():
    global r
    r = calc_c(r)


def set_g():
    global g
    g = calc_c(g)


def set_b():
    global b
    b = calc_c(b)


def clear():
    global r, g, b

    r = calc_c(r)
    g = calc_c(g)
    b = calc_c(b)


def handler(fn):
    @debounce
    def run():
        fn()
        RGBled.fill((r, g, b))
        RGBled.write()

    return run


button_one.irq(trigger=Pin.IRQ_RISING, handler=handler(set_r))
button_two.irq(trigger=Pin.IRQ_RISING, handler=handler(set_g))
button_three.irq(trigger=Pin.IRQ_RISING, handler=handler(set_b))
button_four.irq(trigger=Pin.IRQ_RISING, handler=handler(clear))

while True:
    print(r, g, b)
    time.sleep_ms(50)
