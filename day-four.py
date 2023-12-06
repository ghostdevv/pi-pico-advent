from utils import debouce
from machine import Pin
import time

dec_button = Pin(0, Pin.IN, Pin.PULL_DOWN)
inc_button = Pin(1, Pin.IN, Pin.PULL_DOWN)
onboard_led = Pin(25, Pin.OUT)


class CounterSimple:
    def __init__(self, leds: list[Pin]):
        self.count = 0
        self.leds = leds
        self.set(0)

    def set(self, new_count: int):
        self.count = new_count
        for i, led in enumerate(self.leds):
            led.value(1 if i < self.count else 0)


counter = CounterSimple(
    [
        Pin(9, Pin.OUT),
        Pin(10, Pin.OUT),
        Pin(11, Pin.OUT),
        Pin(12, Pin.OUT),
        Pin(13, Pin.OUT),
    ]
)


@debouce
def increment():
    global counter

    if counter.count < 5:
        counter.set(counter.count + 1)

    print(f"Count is {counter.count}")


@debouce
def decrement():
    global counter

    if counter.count > 0:
        counter.set(counter.count - 1)

    print(f"Count is {counter.count}")


dec_button.irq(handler=decrement, trigger=Pin.IRQ_RISING)
inc_button.irq(handler=increment, trigger=Pin.IRQ_RISING)


while True:
    time.sleep_ms(500)
