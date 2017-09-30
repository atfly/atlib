
#!/usr/bin/env python
#-*-: coding: utf-8 -*-

import subprocess
import sys
import re
import optparse
import pxssh
import os

if sys.hexversion < 0x02040000:
        print >> sys.stderr, 'Your python version is too old (%s)' % \
                                                        (sys.version.split()[0])
        print >> sys.stderr, 'You need at least Python 2.4'
        sys.exit(1)

class RemoteDispatch(object):
	def __init__(self, host, usrname, password):
		self.host = host
		self.usr = usrname
		self.pwd = password

	def login(self):
		self.s=pxssh.pxssh()
		try:
        		self.s.login(self.host, self.usr, self.pwd)
    		except:	
			print "Login %s Failed !" % self.host

	def trasmit_cmd(self, cmdline):
		self.s.sendline(cmdline)
		self.s.prompt()
		
		return self.s.before.strip()

	def logout(self):
		self.s.logout()

class SetEthx(object):
	def __init__(self, host, username, password, options):
		self.opts = options
		self.host = host
		self.remote = RemoteDispatch(self.host, username, password)
		self.sock = self.remote.login()

	def search(self):
		output = self.remote.trasmit_cmd("ethtool -i %s" % self.opts.search)
		for i in output.split('\n')[1:]:
			print i

	def modify(self):
		if self.opts.ip:
			output = self.remote.trasmit_cmd("ifconfig %s" % self.opts.eth)
			content = self.process(output)
			self.remote.trasmit_cmd("echo '%s' > /etc//etc/sysconfig/network-scripts/ifcfg-%s" % (content, self.opts.file))
			self.remote.logout()
		else:
			print "Error ! Please press -i x.x.x.x !"
			sys.exit(1)

	def process(self, output):
		olist = output.split('\n')[1]
		m = re.match(".*HWaddr (.*).*", olist)
		if m:
			hwaddr = m.group(1)
			if hwaddr is None:
				print "have no hwaddr !"
				sys.exit(1)
			else:
				return "DEVICE=%s\nBOOTPROTO=static\nIPADDR=%s\nNETMASK=%sHWADDR=%s\nONBOOT=yes\n" % (self.opts.eth, self.opts.ip, self.opts.mask, hwaddr)	
		else:
			print "Don't finde HWaddr work !"
			sys.exit(1)

def parse_cmd():
	p = optparse.OptionParser(description="ethernet setup", prog="set_ethx", version="1.0", 
			usage="%prog [options] [ethx]")
	p.add_option("-s", "--search", action="store", dest="search", help="search ethernet tpye", 
			type="str")
	p.add_option("-f", "--file", action="store", dest="ifcfg-ethx file", help="modified ifcfg file", 
                        type="str")
	p.add_option("-i", "--ip", action="store", dest="ip", help="setup ip", type="str")
	p.add_option("-e", "--eth", action="store", dest="eth", help="set up ethx", type="str")
	p.add_option("-m", "--mask", action="store", dest="mask", help="set up mask", type="str")
	p.add_option("-l", "--host", action="store", dest="host", help="host name", type="str")
	(opts, args) = p.parse_args()

	return opts, args

def usage():
	print "python set_ethx.py -s ethx -l [host]\npython set_ethx.py -f ethx -i x.x.x.x -m 255.x.x.x -l [host] -e ethx"

def main():
	flag = False
	USERNAME = 'xxx'
	PASSWORD = 'xxxxxxx'
	opts, args = parse_cmd()
	try:
		if opts.host:
			obj = SetEthx(opts.host, USERNAME, PASSWORD, opts)
			if opts.search:
				obj.search()
				flag = True
			if flag == False:
				if opts.file and opts.ip and opts.eth and opts.mask:
					obj.modify()
	except:
		print "set_ethx.py --help"
		usage()
		sys.exit(1)
		
if __name__ == '__main__':
	main()
