# -*- coding=utf-8 -*-
# file: file.py
#

'''
open mode
r w a b +

read readline readlines(list) 
write writelines(list)
'''
#1 read
file=open(r'F:\Develop\Python\basic.py','r')
str=file.read()
print str
file.close()
'''
l=file.readlines()
print l
'''

#2 write
list=['1 what\n','2 is\n','3 your\n','4 name\n','5 ?\n']
file=open(r'F:\Develop\Python\test.txt','w')
file.writelines(list)
file.close()

#3 read(1) in while
file=open(r'F:\Develop\Python\test.txt','r')
while True:
	char=file.read(1)
	if not char:
		break
	# process(char)
file.close()

#4 readline() in while
file=open(r'F:\Develop\Python\test.txt','r')
while True:
	line=file.readline()
	if not line:
		break
	# process(line)
file.close()


