import sys
text = sys.stdin.read()
words = text.split()
print words
wordcount = len(words)
print wordcount

for line in sys.stdin:
	print line
