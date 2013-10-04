import threading
import time

exitFlag = 0

def print_time(threadName,delay,counter):
	while counter:
		if exitFlag:
			thread.exit()
		time.sleep(delay)
		print("{0}: {1}".format(threadName,time.ctime(time.time())))
		counter -=1

class MyThread(threading.Thread):
	"""
	a simple thread
	"""
	def __init__(self,threadID,threadName,delay,counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.threadName = threadName
		self.delay = delay
		self.counter = counter

	def run(self):
		print("Starting {0}".format(self.threadName))
		print_time(self.threadName,self.delay,self.counter)
		print("Exiting {0}".format(self.threadName))

def main():
	thread1 = MyThread(1,'Thread-1',1,5)
	thread2 = MyThread(2,'Thread-2',2,5)
	thread1.start()
	thread2.start()
	# thread.join(): The join() waits for threads to terminate.
	# blocking current main thread
	threads = []
	threads.append(thread1)
	threads.append(thread2)
	for t in threads:
		t.join()
	print('Exiting Main Thread')

if __name__ == "__main__":
	main()
