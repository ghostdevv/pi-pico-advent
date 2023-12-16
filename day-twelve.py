from lib.pico_i2c_led import I2cLcd
from machine import I2C, Pin, UART
from time import sleep_ms

LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16

lcdi2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
lcd = I2cLcd(lcdi2c, 0x27, LCD_NUM_ROWS, LCD_NUM_COLS)

uart = UART(0, 9600)

lcd.putstr("Count: ")
count = 0

while True:
    lcd.move_to(7, 0)
    lcd.putstr(str(count))
    count += 1

    sleep_ms(100)
