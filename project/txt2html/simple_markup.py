import sys,re

def append_empty_line(f):
	'append an empty line to file and create a generator by using yield'
	for l in f:
		yield l
	yield '\n'

def blocks(f):
	'split file into blocks separated by empty line and connect all lines in a block to create a block string and then return a generator'
	b= []
	for l in append_empty_line(f):
		if l.strip():
			b.append(l)
		elif b:
			s = ''.join(b).strip()
			yield s
			b = []

def test_blocks():
	'test blocks function'
	f = open('test_input.txt','r')
	for b in blocks(f):
		print b
	f.close()

def markup():
	'markup input text file'
	print '<html><head><title>A simple markup page</title></head><body>'
	btitle = True
	f = open('test_input.txt','r')
	for b in blocks(f):
		b = re.sub(r'\*(.+?)\*',r'<em>\1</em>',b)
		if btitle:	
			print '<h1>'	
			print b
			print '</h1>'
			btitle = False
		else:
			print '<p>'
			print b
			print '</p>'
	f.close()
	print '</body><html>'

def main():
	#test_blocks()
	markup()

if __name__ =='__main__':
	main()
