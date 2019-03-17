import ZeroSeg.led as led
import time
import RPi.GPIO as GPIO
device = led.sevensegment(cascaded=2)

switch1 = 17
switch2 = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(switch1, GPIO.IN)
GPIO.setup(switch2, GPIO.IN)

number = 0

clockRunning = False

while True:

	number = int(number * 10) / 10

	numStr = str(number) + ".0" if int(number) == number else str(number)

	device.letter(1, 1, numStr[-1])
	device.letter(1, 2, numStr[-3], True)
	if len(numStr) > 3:
		device.letter(1, 3, numStr[-4])
	if len(numStr) > 4:
		device.letter(1, 4, numStr[-5])

	if not GPIO.input(switch1):
		clockRunning = not clockRunning
	elif not GPIO.input(switch2):
		device.clear()
		clockRunning = False
		number = 0

	time.sleep(0.1)

	if clockRunning == True:
		number = number + 0.1
