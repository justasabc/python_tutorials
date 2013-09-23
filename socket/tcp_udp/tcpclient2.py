import socket
s = socket.socket()
host = socket.gethostname()
port = 1234
t = (host,port)
s.connect(t)
print(s.recv(1024))
