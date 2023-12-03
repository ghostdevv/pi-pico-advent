from machine import Pin
import time

onboard_led = Pin(25, Pin.OUT)
red_led = Pin(14, Pin.OUT)

red_led.value(1)
onboard_led.value(0)

while True:
    red_led.toggle()
    onboard_led.toggle()
    time.sleep(0.5)
