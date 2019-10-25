from DaliServer import DaliServer
from threading import Thread
from pythonosc import dispatcher
from pythonosc import osc_server
import queue as q
import time

IP = '192.168.1.46'
PORT = 15200

# c = DaliServer()
# c.send(0, 0)
# time.sleep(4)
# c.send(1, 0)
# time.sleep(1)
# c.close()

def broadcast(addr, scene):
	# global c
	print('messagione osc', scene)
	c = DaliServer();
	c.send(scene)
	time.sleep(1)
	c.close()


def group_message(addr, group, scene):
	# global c
	print('messaggione osc', group, scene)
	c = DaliServer();
	c.send(scene, group)
	time.sleep(1)
	c.close()

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/Raffaello/Lights/GroupMessage", group_message)
dispatcher.map("/Raffaello/Lights/Broadcast", broadcast)

# server = osc_server.ThreadingOSCUDPServer((IP, PORT), dispatcher)
server = osc_server.BlockingOSCUDPServer((IP, PORT), dispatcher)
print("Serving on {}".format(server.server_address))
server.serve_forever()


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