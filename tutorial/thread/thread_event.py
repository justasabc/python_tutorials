import threading
import time

class MyThread(threading.Thread):
	"""
	a simple thread
	"""
	def __init__(self,name,daemon,event):
		threading.Thread.__init__(self)
		self.name = name
		self.daemon = daemon
		self.event = event

	def run(self):
		print("Starting {0}".format(self.name))
		time.sleep(3)
		print("Exiting {0}".format(self.name))
		# set flag to true indicating current thread is finished
		self.event.set()

def main():
	# default flag is false
	event = threading.Event()
	thread1 = MyThread('Thread-1',True,event)
	thread1.start()
	# Block until the internal flag is true
	event.wait()
	print('Exiting Main Thread')

if __name__ == "__main__":
	main()
