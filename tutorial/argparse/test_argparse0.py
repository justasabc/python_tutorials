# site:http://docs.python.org/3/howto/argparse.html
import argparse
parser = argparse.ArgumentParser()
# positional argument
#parser.add_argument("echo", help="echo the string you use here")
#parser.add_argument("square",help="display a square of a given number",type=int)
#optional argument
parser.add_argument('-f', '--file',dest='file', help='set filename')
# short version -v ; long version --version; dest is the variable name that we refered later;action is set to "store_true". This means that, if the option is specified, assign the value True to args.verbose. Not specifying it implies False. 
parser.add_argument('-v', '--verbose',action='store_true',dest='verbose', help='verbose or not')
args = parser.parse_args()
#print(args.echo) 
#print(args.square**2)
if args.verbose:
	print("verbose turned on")
else:
	print("verbose turned off")
print("hello {} you {}".format('xxx',2))
