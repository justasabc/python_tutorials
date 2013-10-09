import subprocess
import sys

# get platform first
WIN = 1
LINUX = 2
MAC = 3

def get_platform():
	if sys.platform.startswith("win32"):
		return WIN
	elif sys.platform.startswith("linux"):
		return LINUX
	elif sys.platform.startswith("darwin"):
		return MAC
	else:
		return LINUX

PLATFORM = get_platform()
# get platform first

def is_host_up(ip):
	"""
	check if host is up
	"""
	if PLATFORM == WIN:
		pingstr="ping -n 1 -i 1 {0}".format(ip)
	else:
		pingstr="ping -c 1 -t 1 {0}".format(ip)
	ret = subprocess.call(pingstr, shell=True, stdout=open('/dev/null','w'), stderr=subprocess.STDOUT)
	if (ret == 0): # 0 means ping success
		return True
	return False

def test_platform():
	print("test platform")
	print(PLATFORM)
	ip = "192.168.1.200"
	print(is_host_up(ip))
	ip = "192.168.1.198"
	print(is_host_up(ip))

def main():
	test_platform()

if __name__=="__main__":
	main()
