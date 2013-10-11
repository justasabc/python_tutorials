import Queue
import threading
import time

exitFlag = 0
queueLock = threading.Lock()

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name

"""
Queue.task_done()
Indicate that a formerly enqueued task is complete. Used by queue consumer threads. For each get() used to fetch a task, a subsequent call to task_done() tells the queue that the processing on the task is complete.
Queue.join()
Blocks until all items in the queue have been gotten and processed.
The count of unfinished tasks goes up whenever an item is added to the queue. The count goes down whenever a consumer thread calls task_done() to indicate that the item was retrieved and all work on it is complete. When the count of unfinished tasks drops to zero, join() unblocks.
"""
def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
	if not q.empty():
        	data = q.get()
        	print "%s processing %s" % (threadName, data)
        	queueLock.release()
		# task_done + join
		q.task_done()
	else:
		queueLock.release()
        time.sleep(1)

def main():
	threadList = ["Thread-1", "Thread-2", "Thread-3"]
	nameList = ["One", "Two", "Three", "Four", "Five"]
	workQueue = Queue.Queue(10)
	threads = []
	threadID = 1

	# Create new threads
	for tName in threadList:
    		thread = myThread(threadID, tName, workQueue)
    		thread.start()
    		threads.append(thread)
    		threadID += 1

	# Fill the queue
	queueLock.acquire()
	for word in nameList:
    		workQueue.put(word)
	queueLock.release()

	# Wait for queue to empty
	#while not workQueue.empty():
    	#	pass
	# wait for queue jobs to finish
	workQueue.join()

	# Notify threads it's time to exit
	global exitFlag
	exitFlag = 1

	# Wait for all threads to complete
	for t in threads:
    		t.join()
	print "Exiting Main Thread"

if __name__ == "__main__":
	main()
