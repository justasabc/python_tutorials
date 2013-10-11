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

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not q.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data)
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
	while not workQueue.empty():
    		pass

	# Notify threads it's time to exit
	global exitFlag
	exitFlag = 1

	# Wait for all threads to complete
	for t in threads:
    		t.join()
	print "Exiting Main Thread"

if __name__ == "__main__":
	main()