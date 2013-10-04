import threading
import time
import Queue

exitFlag = 0
queueLock = threading.Lock()

def process_data(threadName,q):
	while not exitFlag:
		# lock for accesss workQueue in child threads
		queueLock.acquire()
		if not q.empty():
			data = q.get()
			queueLock.release()
			print('{0} processing {1}'.format(threadName,data))
		else:
			queueLock.release()
		time.sleep(1)

class MyThread(threading.Thread):
	"""
	a simple thread
	"""
	def __init__(self,threadID,threadName,q):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.threadName = threadName
		self.q = q

	def run(self):
		print("Starting {0}".format(self.threadName))
		process_data(self.threadName,self.q)
		print("Exiting {0}".format(self.threadName))

def main():
	threadList = ['Thread-1','Thread-2','Thread-3']
	dataList = ['one','two','three','four','five']
	workQueue = Queue.Queue(10)
	threads = []
	threadID = 1
	# create new threads
	for tname in threadList:
		thread = MyThread(threadID,tname,workQueue)
		thread.start()
		threads.append(thread)
		threadID +=1

	# fill the queue
	# lock for accesss workQueue in main thread
	queueLock.acquire()
	for data in dataList:
		workQueue.put(data)
	queueLock.release()

	# wait for queue to be empty
	while not workQueue.empty():
		pass

	# notify threads it's time to exit
	exitFlag = 1

	# wait for threads to terminate
	# thread.join(): The join() waits for threads to terminate.
	# blocking current main thread
	for t in threads:
		t.join()
	print('Exiting Main Thread')

if __name__ == "__main__":
	main()
