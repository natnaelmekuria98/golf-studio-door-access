# raspberry-pi/door_control.py
from gpiozero import OutputDevice
from time import sleep

class DoorControl:
    def __init__(self, pin=17):
        self.motor = OutputDevice(pin)

    def open(self):
        self.motor.on()
        sleep(5)  # Keep door open for 5 seconds
        self.motor.off()
