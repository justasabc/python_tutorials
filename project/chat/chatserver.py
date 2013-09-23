# Note: run this server by using python2.7 instead of python3.2
from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

IP = ''
PORT = 5555
SEP = '\n'

class ChatSession(async_chat):
	"""
	A simple chat session corresponding to a client
	"""
	def __init__(self,sock):
		async_chat.__init__(self,sock)
		self.set_terminator(SEP)
		self.data = []

	def collect_incoming_data(self, data):
		print("---------------collect_incoming_data")
		self.data.append(data)

	def found_terminator(self):
		print("---------------found_terminator")
		line = ''.join(self.data)
		self.data = []
		print(line)

class ChatServer(dispatcher):
	"""
	a simple chat server.
	a server has n clients and n sessions.
	"""
	def __init__(self, ip,port):
		dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.bind((ip,port))
		self.listen(5)
		# store all sessions
		self.sessions = []

	def handle_accept(self):
		conn, addr = self.accept()
		print("Connection from {0}".format(addr))
		# create and store session
		cs = ChatSession(conn)
		self.sessions.append(cs)

if __name__ == '__main__':
	s = ChatServer(IP,PORT)
	try: 
		asyncore.loop()
	except KeyboardInterrupt: 
		pass
