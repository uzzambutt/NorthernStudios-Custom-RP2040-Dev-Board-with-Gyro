import time
from machine import Pin

# Define the onboard LED pin (usually GP25 for Pico)
led = Pin(25, Pin.OUT)

while True:
    led.value(1) # Turn LED ON
    time.sleep(0.5)
    led.value(0) # Turn LED OFF
    time.sleep(0.5)
