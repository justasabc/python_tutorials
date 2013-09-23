f = open('1.txt','r+')
try:
	f.write('hello welcome to my place\n')
finally:
	f.close()

with open('1.txt','r+') as fi:
	fi.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
	fi.close()
