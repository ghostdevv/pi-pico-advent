from machine import Pin
import time

onboard_led = Pin(25, Pin.OUT)
red_led = Pin(14, Pin.OUT)

green_button = Pin(3, Pin.IN, Pin.PULL_DOWN)
red_button = Pin(2, Pin.IN, Pin.PULL_DOWN)

red_led.value(0)
onboard_led.value(0)

while True:
    onboard_led.value(green_button.value())
    red_led.value(red_button.value())
