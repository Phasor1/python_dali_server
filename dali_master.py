# from __future__ import print_function
# from __future__ import unicode_literals
# from dali.command import from_frame
from dali.driver.tridonic import AsyncTridonicDALIUSBDriver
from dali.address import Group
from dali.gear.general import GoToScene, _StandardCommand, DAPC
import logging

import signal
import sys
import time

# DALI USB CONTROLLER
DALI_USB_VENDOR = 0x17B5
DALI_USB_PRODUCT = 0x0020

driver = AsyncTridonicDALIUSBDriver()
def signal_handler(signal, frame):
        driver.backend.close()
        sys.exit(0)
 # async response callback
def response_received(response):
    print('Response received: {}'.format(response))

def send_async(logger, command):
    global driver
    print('Test async driver')
    driver.logger = logger
    driver.debug = True

    driver.send(command, callback=response_received)

    # exit callback
# setup console logging
logger = logging.getLogger('TridonicDALIDriver')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
))
logger.addHandler(handler)

# command to send
# command = GoToScene(Group(0), 0)
send_async(logger, GoToScene(Group(0), 0))
time.sleep(1)
send_async(logger, GoToScene(Group(0), 1))
