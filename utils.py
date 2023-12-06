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
