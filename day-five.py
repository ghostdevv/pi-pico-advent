from utils import CounterSimple
from machine import Pin
import time

switch_one = Pin(4, Pin.IN, Pin.PULL_DOWN)
switch_two = Pin(3, Pin.IN, Pin.PULL_DOWN)
switch_three = Pin(2, Pin.IN, Pin.PULL_DOWN)
switch_four = Pin(1, Pin.IN, Pin.PULL_DOWN)
switch_five = Pin(0, Pin.IN, Pin.PULL_DOWN)

counter = CounterSimple(
    [
        Pin(9, Pin.OUT),
        Pin(10, Pin.OUT),
        Pin(11, Pin.OUT),
        Pin(12, Pin.OUT),
        Pin(13, Pin.OUT),
    ]
)

while True:
    # binary mode
    value = switch_one.value()
    value = value + 2 if switch_two.value() else value
    value = value + 4 if switch_three.value() else value
    value = value + 8 if switch_four.value() else value
    value = value + 16 if switch_five.value() else value

    # decimal mode
    # value = (
    #     switch_one.value()
    #     + switch_two.value()
    #     + switch_three.value()
    #     + switch_four.value()
    #     + switch_five.value()
    # )

    counter.set(value)

    print(
        f"{switch_one.value()} {switch_two.value()} {switch_three.value()} {switch_four.value()} {switch_five.value()} {value}"
    )

    time.sleep_ms(200)
