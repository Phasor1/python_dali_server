from dali.driver.tridonic import AsyncTridonicDALIUSBDriver
from dali.address import Group, Broadcast
from dali.gear.general import GoToScene, _StandardCommand, DAPC
import logging

import signal
import sys
import time

class DaliServer():
	def __init__(self):
		self.driver = AsyncTridonicDALIUSBDriver();
		self.driver.logger = logging.getLogger('TridonicDALIDriver')
	def signal_handler(self):
		self.driver.backend.close()
		sys.exit(0)

	def close(self):
		print('closing usb communication')
		signal.signal(signal.SIGINT, self.signal_handler)
	 # async response callback
	def response_received(self, response):
	    print('Response received: {}'.format(response))

	def send(self, scene=0, group=None):
		self.driver.debug = True
		if group is not None:
			print('group {} go to scene {}'.format(group, scene))
			self.driver.send(GoToScene(Group(group), scene))
		else:
			print('broadcasting scene ' + str(scene))
			self.driver.send(GoToScene(Broadcast(), scene))
		# self.driver.send(command, callback=self.response_received)
