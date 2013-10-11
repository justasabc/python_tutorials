#!/usr/bin/env python

import pycurl
import StringIO
import simplejson as json
from pkg_resources import parse_version
# user defined
import notify

APP_VERSION = '0.01'

def get_version():
	return APP_VERSION

def new_version():
	# Get current version
	c = pycurl.Curl()
	b = StringIO.StringIO()
	c.setopt(pycurl.URL, "http://dewdrop.deepcode.net/version.php?v=%s" % get_version())
	c.setopt(pycurl.WRITEFUNCTION, b.write)
	c.perform()
	# {"version": "0.10", "url": "http://dewdrop.deepcode.net"}
	res = json.loads(b.getvalue())
	current = res.get('version')
	if parse_version(current) > parse_version(APP_VERSION):
		# Version is different
		notify.update(res.get('url'))
	return True

def test_parse_version():
	print parse_version("0.10") > parse_version("0.01")
	print parse_version("0.20") > parse_version("0.10.1")

if __name__ == "__main__":
	new_version()
