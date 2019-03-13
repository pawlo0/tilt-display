import ZeroSeg.led as led
import time
device = led.sevensegment(cascaded=2)

device.show_message("SCROLLING MESSAGE")
