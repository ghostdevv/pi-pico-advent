from machine import Pin
import time


def debouce(fn):
    last_interrupt_time = time.ticks_ms()

    def run(pin: Pin):
        nonlocal last_interrupt_time

        if time.ticks_diff(time.ticks_ms(), last_interrupt_time) > 300:
            last_interrupt_time = time.ticks_ms()
            fn()

    return run


class CounterSimple:
    def __init__(self, leds: list[Pin]):
        self.count = 0
        self.leds = leds
        self.set(0)

    def set(self, new_count: int):
        self.count = new_count
        for i, led in enumerate(self.leds):
            led.value(1 if i < self.count else 0)
