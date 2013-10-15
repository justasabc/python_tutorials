# http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner
"""

@classmethod means: when this method is called, we pass the class as the first argument instead of the instance of that class (as we normally do with methods). This means you can use the class and its properties inside that method rather than a particular instance.

@staticmethod means: when this method is called, we don't pass an instance of the class to it (as we normally do with methods). This means you can put a function inside a class but you can't access the instance of that class (this is useful when your method does not use the instance).

If what you want is a Factory method that is aware of the class that called it, then @classmethod is what you need.
"""

class Date:

	def __init__(self, month, day, year):
  		self.month = month
  		self.day   = day
  		self.year  = year

  	def display(self):
    		print "{0}-{1}-{2}".format(self.month, self.day, self.year)

	@classmethod
    	def from_string(cls, date_as_string):
		# Factory function
        	month, day, year = map(int, date_as_string.split('-'))
        	date1 = cls(month, day, year)
        	return date1

	@staticmethod
    	def is_date_valid(date_as_string):
        	day, month, year = map(int, date_as_string.split('-'))
        	try:
            		assert 0 <= day <= 31
            		assert 0 <= month <= 12
            		assert 0 <= year <= 3999
        	except AssertionError:
            		return False
        	return True

class MyDate(Date):
	def display(self):
      		print "{0}-{1}-{2} - 00:00:00PM".format(self.month, self.day, self.year)


def main():
	d = Date(1,1,2013)
	d.display()
	print isinstance(d,Date)

	d = Date.from_string('10-22-2013')
	d.display()
	print isinstance(d,Date)

	print  Date.is_date_valid('10-32-2013')

	print('-'*30)
	d = MyDate(1,1,2013)
	d.display()
	print isinstance(d,MyDate)

	d = MyDate.from_string('10-22-2013')
	d.display()
	print isinstance(d,MyDate)

	print  MyDate.is_date_valid('10-32-2013')

if __name__=="__main__":
	main()
