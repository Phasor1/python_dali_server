from DaliServer import DaliServer
from threading import Thread
from pythonosc import dispatcher
from pythonosc import osc_server
import queue
import time

IP = '192.168.1.46'
PORT = 15200

q = queue.Queue()
# c = DaliServer()
# c.send(0, 0)
# time.sleep(4)
# c.send(1, 0)
# time.sleep(1)
# c.close()

def broadcast(addr, scene):
	# global c
	print('messagione osc', scene)
	q.put('broadcast-' + str(scene))


def group_message(addr, group, scene):
	# global c
	print('messaggione osc', group, scene)
	q.put('group-' + str(group) + '-' + str(scene))
	
def lightValue(addr, lv):
	print('messaggione osc', lv)
	q.put('DAPC-' + str(lv))

def main_thread():

	disp = dispatcher.Dispatcher()
	disp.map("/Raffaello/Lights/GroupMessage", group_message)
	disp.map("/Raffaello/Lights/Broadcast", broadcast)
	disp.map("/Raffaello/Lights/lightValue", lightValue)

	server = osc_server.ThreadingOSCUDPServer((IP, PORT), disp)
	# server = osc_server.BlockingOSCUDPServer((IP, PORT), dispatcher)
	print("Serving on {}".format(server.server_address))
	server.serve_forever()

main = Thread(target=main_thread)
main.start()
c = DaliServer();
while True:
	el = q.get()
	if 'group' in el:
		el, group, scene  = el.split('-')
		# c = DaliServer();
		c.send(int(scene), int(group))
		# c.close()
	elif 'broadcast' in el:
		el, scene = el.split('-')
		# c = DaliServer();
		c.send(int(scene), int(group))
	elif 'DAPC':
		cmd, val = el.split('-')
		c.DAPC(int(val))
		# c.close()
# def trottler_close():
# 	c = DaliServer()
# 	c.send(1, 0)
# 	c.close()
# 	time.sleep(0.1)
# 	# exit()

# def trottler_open():
# 	c = DaliServer()
# 	c.send(0, 0)
# 	c.close()
# 	time.sleep(0.1)
	# exit()

# c = DaliServer();
# queue = q.Queue()

# t1 = Thread(target=trottler_open, )
# t2 = Thread(target=trottler_close, )

# queue.put(c)
# t1.start()
# t1.join()
# queue.put(c)1
# queue.put(c)
# time.sleep(0.5)
# t2.start()
# t2.join()
# c.close()