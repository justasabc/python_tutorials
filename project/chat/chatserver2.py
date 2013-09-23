# Note: run this server by using python2.7 instead of python3.2
from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

IP = ''
PORT = 5555
SEP = '\n'
NAME = 'TestChat'

class ChatSession(async_chat):
	"""
	A simple chat session corresponding to a client
	"""
	def __init__(self,sock,server):
		async_chat.__init__(self,sock)
		self.set_terminator(SEP)
		self.data = []
		# save server of this session
		self.server = server
		# send message to client of this session
		self.push('Welcome to {0}\n'.format(self.server.name))

	def collect_incoming_data(self, data):
		print("---------------collect_incoming_data")
		self.data.append(data)

	def found_terminator(self):
		print("---------------found_terminator")
		line = ''.join(self.data)
		self.data = []
		print(line)
		# broadcast message from this session to all other sessions
		except_list = []
		except_list.append(self)
		self.server.broadcast(line,except_list)

	def handle_close(self):
		print("---------------handle_close")
		async_chat.handle_close(self)
		# remove this session from server's session list
		self.server.disconnect(self)


class ChatServer(dispatcher):
	"""
	a simple chat server.
	a server has n clients and n sessions.
	"""
	def __init__(self, ip,port,name):
		dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.bind((ip,port))
		self.listen(5)
		self.name = name
		# store all sessions
		self.sessions = []

	def handle_accept(self):
		conn, addr = self.accept()
		print("Connection from {0}".format(addr))
		# create and store session
		cs = ChatSession(conn,self)
		self.sessions.append(cs)

	def broadcast(self,msg,except_list):
		print("----------------broadcast messages")
		for session in self.sessions:
			if not session in except_list:
				session.push(msg+SEP)

	def disconnect(self,session): 
		print("----------------disconnect client from server")
		self.sessions.remove(session)

if __name__ == '__main__':
	s = ChatServer(IP,PORT,NAME)
	try: 
		asyncore.loop()
	except KeyboardInterrupt: 
		pass
