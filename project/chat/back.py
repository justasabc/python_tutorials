# Note: run this server by using python2.7 instead of python3.2
from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

# session.push('hello\n')
# 	broadcast('hello\n')
# print('hello')

IP = ''
PORT = 5555
BACKLOG = 5 # 0-5
RN = '\n'
SPACE = ' '
PREFIX = 'do_'
NAME = 'TestChat'

class EndSession(Exception):
	pass

class CommandHandler:
	"""
	command handler similar to cmd.CMD
	"""
	def unknown(self,session,cmd):
		session.push('Unknown command: {0}{1}'.format(cmd,RN))

	def handle(self,session,line):
		#print('---------------Handle cmd-----------------')
		if not line.strip():
			return
		parts = line.split(SPACE,1)
		cmd = parts[0].strip()
		#cmd = parts[0]
		try:
			line = parts[1].strip()
		except IndexError:
			line = ''
		method = getattr(self,PREFIX+cmd,None)
		try:
			#print(cmd,line)
			method(session,line)
		except TypeError:
			self.unknown(session,cmd)

class Room(CommandHandler):
	"""
	a room contains n client sessions and handles commands
	"""
	def __init__(self,server):
		self.server = server
		self.sessions = []

	def add(self,session):
		self.sessions.append(session)

	def remove(self,session):	
		self.sessions.remove(session)

	def broadcast(self,line):
		for session in self.sessions:
			session.push(line)

class LoginRoom(Room):
	"""
	room for login users
	"""
	def add(self,session):
		Room.add(self,session)
		self.broadcast('Welcome to {0}{1}'.format(self.server.name,RN))

	def unknown(self,session,cmd):
		session.push('Please log in by using{0}login <name>{0}'.format(RN))
	
	def do_login(self,session,line):
		name = line.strip()
		if not name:
			session.push('Please enter a name{0}'.format(RN))
		elif name in self.server.users:
			session.push('The name {0} is used{1}'.format(name,RN))
			session.push('Please try again{0}'.format(RN))
		else:
			# save session's name and enter main room
			session.name = name
			session.enter(self.server.main_room)

class ChatRoom(Room):
	"""
	main chat room
	"""
	def add(self,session):
		self.broadcast('{0} has entered the room{1}'.format(session.name,RN))
		# save users and sessions in server
		self.server.users[session.name] = session
		print('User {0} has entered the room'.format(session.name))
		Room.add(self,session)

	def remove(self,session):
		Room.remove(self,session)
		self.broadcast('User {0} has left the room{1}'.format(session.name,RN))
		print('User {0} has left the room'.format(session.name))

	def unknown(self,session,cmd):
		session.push('Unknown command: {0}{1}'.format(cmd,RN))
		session.push('Available commands:{0}'.format(RN))
		session.push('say <msg>{0}'.format(RN))
		session.push('look {0}'.format(RN))
		session.push('who {0}'.format(RN))
		session.push('logout {0}'.format(RN))

	def do_say(self,session,line):
		if line.strip():
			self.broadcast('{0}: {1}{2}'.format(session.name,line,RN))

	def do_look(self,session,line):
		session.push('The following are in this room:{0}'.format(RN))
		for other in self.sessions:
			session.push('{0}{1}'.format(other.name,RN))

	def do_who(self,session,line):
		session.push('The following are logged in:{0}'.format(RN))
		for name in self.server.users:
			session.push('{0}{1}'.format(name,RN))

	def do_logout(self,session,line):
		raise EndSession

class LogoutRoom(Room):
	"""
	for logout users and remove user from server
	"""
	def add(self,session):
		try:
			del self.server.users[session.name]
		except KeyError:
			pass

class ChatSession(async_chat):
	"""
	A simple chat session corresponding to a client
	"""
	def __init__(self,sock,server):
		async_chat.__init__(self,sock)
		self.server = server
		self.set_terminator(RN)
		self.data = []
		self.name = None
		self.room = None # record which kind of room
		# all sessions start with LoginRoom
		self.enter(LoginRoom(self.server))

	def enter(self,room):
		# remove self from current room and add self to the next room
		#try:
		#	cur = self.room
		#except AttributeError:
		#	pass
		#else:
		#	cur.remove(self)
		if self.room:
			self.room.remove(self)
		self.room = room
		room.add(self)

	def collect_incoming_data(self, data):
		self.data.append(data)

	def found_terminator(self):
		line = ''.join(self.data)
		self.data = []
		print(line)
		# handle commands
		try:
			self.room.handle(self,line)
		except EndSession: # do_logout
			self.handle_close()

	def handle_close(self):
		async_chat.handle_close(self)
		# enter logout room
		self.enter(LogoutRoom(self.server))


class ChatServer(dispatcher):
	"""
	a simple chat server.
	a server has n client users and n sessions.
	a server has n chat rooms
	in this example, this server has only 1 main room
	"""
	def __init__(self, ip,port,backlog,name):
		dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.bind((ip,port))
		self.listen(backlog)
		self.name = name
		# store all users and sessions in a dict like: name session
		self.users = {}
		# stotr main room
		self.main_room = ChatRoom(self)

	def handle_accept(self):
		conn, addr = self.accept()
		print("Connection from {0}".format(addr))
		# create a user session for every connection
		ChatSession(conn,self)

def main():
	s = ChatServer(IP,PORT,BACKLOG,NAME)
	try: 
		print('Server is running...')
		asyncore.loop()
	except KeyboardInterrupt: 
		pass

if __name__ == '__main__':
	main()
