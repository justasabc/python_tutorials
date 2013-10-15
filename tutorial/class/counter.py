# class-level 
# instance-level

class Test(object):
	counter = 0
	
	def __init__(self):
		# instance-level
		self.counter +=1

def test1():
	t1 = Test()
	print t1.counter # 1
	print Test.counter # 0
	t2 = Test()
	print t2.counter # 1
	print Test.counter # 0

class Test2(object):
	counter = 0
	
	def __init__(self):
		# class-level
		self.__class__.counter +=1

def test2():
	t1 = Test2()
	print Test2.counter # 1
	print t1.counter # 1
	t2 = Test2()
	print Test2.counter # 2
	print t2.counter # 2
	t3 = Test2()
	print Test2.counter # 3
	print t3.counter # 3

def main():
	print "test1"
	test1()
	print "test2"
	test2()

if __name__=="__main__":
	main()

