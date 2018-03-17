#!/usr/bin/python
import time
import simpleusbrelay

# initialize the library with the idVendor and Product id
relaycontroller=simpleusbrelay.simpleusbrelay(Vendor=0x16c0, Product=0x05df)
#turn on relay 1
relaycontroller.array_on(2)
relaycontroller=None
relaycontroller=simpleusbrelay.simpleusbrelay(Vendor=0x16c0, Product=0x05df)
time.sleep(1)
#turn of relay 1
relaycontroller.array_off(2)
