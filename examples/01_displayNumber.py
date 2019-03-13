import ZeroSeg.led as led
import time
device = led.sevensegment()

device.write_number(deviceId=0, value=1234)
time.sleep(5)
device.clear()
