# -*- coding:utf-8 -*-
# file: first.py
#

# hello world 
print 'hello,world!'

# basic types
str='hello,string'
tuple=('a','b','c')
list=[1,2,3,4,5]
dic={'key1':100,'key2':200}
print str
print tuple
print list
print dic

# 3 ways to comment£º#   '''   '''   """   """

# input /raw_input
'''
name=raw_input('please input your name:')
print name

year=input('plese input the year:')
print year*100
'''

# string
#1 string copy
stra='string a'
strb='string b'
strc=stra # shadow copy
strd=strb[:] # deep copy

#2 string format
'''
format % value
%s %d %f
tag width.demical   
10.2f  .5s
* to number
*.*f  .%s
tag=0  +  - space
010.2f  -10.2f
'''
format1='hello,%s'
value1='kezunlin'
print format1 % value1

format2='%s  is %d years old'
value2=('kezunlin',22)
print format2 % value2

print '%10.2f' % 3.1415926
# use * to replace number
print '%*.*f' % (10,2,3.1415926)

print '%.2s' % 'kezunlin'
# use * to replace number
print '%.*s' % (2,'kezunlin')

# use - to left align
print '%-10.2f' % 3.1415926

#3 string to int
# int() / string.atoi()
str_int='100'
print int(str_int)*2

#4 raw string
raw_string=r'C:\Program Files\Vim'
print raw_string

# basic flow
a=3
b=4
# if else
if a>b:
	print a
else:
	print b

# if elif else
if a>b:
	print a
elif a<b:
	print b
else:
	print 'a==b'

# for 
list2=[0,1,2,3,4]
for i in list2:
	print i
for i in range(0,5):
	print i

# while
x=0
while x<5:
	print x
	x+=1

# function
#1 solid arg
def myadd(x,y):
	return x+y
print myadd(1,2)
print myadd(y=2,x=1)

#2 variable arg  (using * before arg)
def myadd_list(*list):
	r=0
	for i in list:
		r+=i
	return r
print myadd_list(1,2)
print myadd_list(1,2,3)
print myadd_list(1,2,3,4)

#lambda expression
# lambda arg1,agr2:expression
myfun_add=lambda x,y:x+y
print myfun_add(1,2)

#module 
'''
import ways
import module [as new_module]    (use: module.fun)
from module import fun [as new_fun]
'''

# class 
'''
1 the first arg of all funs must be 'self',but there is no need to pass when called.
2 private attribute and method must be started with '__',for example '__XXX'.
3 special method looks like '__XXX__',such as __init__,__del__,__len__.
4 class C(A,B)
'''
class Student:
	name=''
	__score=0
	def __init__(self,name,score):
		self.name=name
		self.__score=score
	def __empty(self,item):
		if item=='':
			return 1
		else:
			return 0
	def show(self):
		if self.__empty(self.name): # NOTICE HERE!
			print 'name empty!'
		else:
			print self.name
		print self.__score
	def setscore(self,score):
		self.__score=score
	def getscore(self):
		return self.__score

#class usage
stu=Student('kezunlin',98)
stu.show()
stu.setscore(100)
print stu.getscore()
stu.show()

# exception
'''
try except else
try finally
except usage
1 except:
2 except ex [,data]:
3 except (ex1,ex2) [,data]:
'''
l=[1,2,3]
#1
try:
	l[3]
except IndexError,Error:
	print Error
else:
	print 'NO ERROR!'

#2
try:
	l[2]/0
except ZeroDivisionError,Error:
	print Error
else:
	print 'NO ERROR!'

#3
try:
	l[3]/0
except (IndexError,ZeroDivisionError),Error:
	print Error
else:
	print 'NO ERROR!'


#raise exception
'''
1 raise ex [,data]
2 raise A  (calss A(Exception))
'''
#1
try:
	raise  Exception,'Kezunlin raise an exception!'
except Exception,data:
	print data
else:
	print 'NO ERROR!'

#2
class MyError(Exception):
	def __init__(self,data):
		self.data=data
	def __str__(self):
		return self.data
try:
	raise  MyError,'Kezunlin raise MyError!'
except MyError,data:
	print data
else:
	print 'NO ERROR!'

# iterator
class TestIterator:
	value=0
	def next(self):
		self.value+=1
		if self.value>10:
			raise StopIteration
		return self.value
	def __iter__(self):
		return self
# test
ti=TestIterator()
for i in ti:
	print i
# 1,2...10


