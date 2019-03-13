import ZeroSeg.led as led
import time
import RPi.GPIO as GPIO
device = led.sevensegment()

switch1 = 17
switch2 = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(switch1, GPIO.IN)
GPIO.setup(switch2, GPIO.IN)

number = 10

while True:
	device.write_number(deviceId=0, value=number)

	if not GPIO.input(switch1):
		number = number -1
	elif not GPIO.input(switch2):
		number = number +1

	time.sleep(0.2)

