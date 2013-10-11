
def max(a,b):
	if a>b:
		return a
	else:
		return b

print max(6,5)

'''
This is a comment.
Use print to output what you want.
'''
print 'hello,world!' # this is a comment
"""
This is a comment.
Use print to output what you want.
"""

list=[1,2,3,4,5,6,7,8,9,10]
list[0:3]
list[7:10]
list[-4:-1]
list[-4:]
list[:]

n=1
if n==1:
	print 'true'
else:
	pass

person='a'
if person=='a':
	status=1
elif person=='b':
	status=2
else:
	status=0

person='a'
status_map={'a':1,'b':2}
status=status_map.get(person,0)

list=[1,2,3,4,5,6,7,8,9,10]
for l in list:
	print l

x=1
while x<=10:
	print x
	x+=1


for l in range(10):
	print l


s=0
for i in xrange(100000):
	if i%19==0:
		s=s+i
print s

r=[1,3,10,98,-2,48]
for i in r:
	if i<0:
		print 'input contains negative value!'
		break
	else:
		pass
else:
	print 'input is OK'

def square(x):
	'calculate the square of x'
	return x*x
print square.__doc__
print square(5)

def fixed_args(a,c,b):
	return 'a=%s,b=%s,c=%s' % (a,b,c)
print fixed_args('ke',100,[1,2])
# a=ke,b=[1,2],c=100

def var_args(a,*args):
	return 'a=%s,args=%s' % (a,args)
print var_args('ke',1,2,3)
# a=ke,args=(1,2,3)

def keyword_args(a,**kwargs):
	return 'a=%s,kwargs=%s' % (a,kwargs)
print keyword_args('ke',k1=1,k2=2)
# a=ke,kwargs={'k1':1,'k2':2}

def default_args(a,b='bar',c=100):
	return 'a=%s,b=%s,c=%s' % (a,b,c)
print default_args('apa') # use default value
#print default_args() # bombs
print default_args(c='car',a='apa') # override order


def square(x):
	if type(x)==type(1):
		return x*x
print square(2) # 4
print square('a') # None

fun=lambda x,y:x+y
print fun(2,3) # 5

def fun(x,y):
	return x+y
print fun(2,3) # 5

import math
print math.sqrt(9)

from math import sqrt
print sqrt(9)



# mymath.py
def mysquare(x):
	return x*x
# self test
if __name__=='__main__':
	print mysquare(5)

class Person:
	name=''
	__age=0
	def __init__(self,name,age):
		self.name=name
		self.__age=age
	def show(self):
		print self.name,self.__age
p=Person('ke',22)
p.show()

class Shape:         # base class
	def is_round(self):
		return True

class Circle(Shape): # inherits shape
	# some code here

class Rect(Shape):   # inherits shape
	def is_round(self): # override method 
		return False

shapes=[Shape(),Circle(),Rect()]
for s in shapes:
	print s.is_round()
# True,True,False


