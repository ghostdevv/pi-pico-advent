from utils import debouce
from machine import Pin
import time

onboard_led = Pin(25, Pin.OUT)
red_led = Pin(14, Pin.OUT)

green_button = Pin(3, Pin.IN, Pin.PULL_DOWN)
red_button = Pin(2, Pin.IN, Pin.PULL_DOWN)

red_led.value(0)
onboard_led.value(0)

red_on = False
green_on = False


def toggle_green():
    global green_on
    green_on = not green_on


def toggle_red():
    global red_on
    red_on = not red_on


green_button.irq(handler=debouce(toggle_green), trigger=Pin.IRQ_RISING)
red_button.irq(handler=debouce(toggle_red), trigger=Pin.IRQ_RISING)

while True:
    time.sleep_ms(500)

    if green_on:
        onboard_led.toggle()
    else:
        onboard_led.value(0)

    if red_on:
        red_led.toggle()
    else:
        red_led.value(0)
