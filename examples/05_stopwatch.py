import ZeroSeg.led as led
import time
import RPi.GPIO as GPIO
device = led.sevensegment()

switch1 = 17
switch2 = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(switch1, GPIO.IN)
GPIO.setup(switch2, GPIO.IN)

number = 0

clockRunning = False

while True:
	device.write_number(deviceId=0, value=number)

	if not GPIO.input(switch1):
		clockRunning = not clockRunning
	elif not GPIO.input(switch2):
		clockRunning = False
		number = 0

	time.sleep(1)

	if clockRunning == True:
		number = number + 1
