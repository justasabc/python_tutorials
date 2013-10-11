import thread
import time

# define a function for the thread
def print_time(threadName,delay):
	count = 0
	while count<5:
		time.sleep(delay)
		count +=1
		print("{0}:{1}".format(threadName,time.ctime(time.time())))

# create two threads as follows
try:
	thread.start_new_thread(print_time,("thread-1",2))
	thread.start_new_thread(print_time,("thread-2",4))
except:
	print("eror: unable to start thread")

while 1:
	pass
