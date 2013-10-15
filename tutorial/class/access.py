# add __ to method to make if inaccessible

class Test(object):
	def __inaccessible(self):
		print "Bet you can not see me"

	def accessible(self):
		print "The secret message is:"
		self.__inaccessible()

def main():
	t = Test()
	t.accessible()
	# not recommended
	print('use _Test__inaccessible')
	t._Test__inaccessible()

if __name__=="__main__":
	main()
