import ZeroSeg.led as led
import time
device = led.sevensegment(cascaded=2)

device.write_text(1, "JOANA")

time.sleep(5)
device.clear()
