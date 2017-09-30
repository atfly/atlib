
#!/usr/bin/env python
#-*-: coding: utf-8 -*-

import optparse
import subprocess
import sys
import locale
import os

class Apt(object):
	def __init__(self, opts):
		self.options = opts

	def apt_install(self, opts, listone=""):
		soft = opts.install if listone == "" else listone
		os.system("apt-get install %s" % soft)

	def apt_search(self, opts):
		list_buf = []
		cout = 0
		ret = subprocess.Popen("apt-cache search %s | awk -F' ' '{print $1}'" % opts.search, shell=True,
					stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		if ret == 0:
			print "commad error !"
			sys.exit(125)
		output = ret.stdout.readlines()
		print '-'*31
		for out in output:
			print "%d\t%s" % (cout, out.strip())
			list_buf.append(out.strip())
			cout += 1
		print '-'*10 + "DONE!" + '-'*10
		if opts.quiet:			
			sys.exit(0)
		else:
			try:
				num = input("Intput software number : ")
			except KeyboardInterrupt:
				print "\tUser press Ctrl+C ,Exit\n"
				sys.exit(125)

			if num > len(list_buf) and num < 0:
				print "number is not right !"
				sys.exit(125)
			else:
				self.apt_install(opts, listone=list_buf[num])

	def run(self):
		if self.options.install:
			self.apt_install(self.options)
		elif self.options.search:
			self.apt_search(self.options)

def parse_cmdline():#www.iplaypy.com
	p = optparse.OptionParser(description="easy apt tool", prog="apt-tool", version="1.0", 
					usage="%prog [options] dest")
	p.add_option("-i", "--install", action="store", dest="install", help="software name", type="string")
	p.add_option("-s", "--search", action="store", dest="search", help="search software", type="string")
	p.add_option("-q", "--quiet", action="store_true", dest="quiet", help="don't install")
	
	(opts, args) = p.parse_args()
	
	if not opts.install and not opts.search:
		print sys.argv[0] + "[-i|-s]" + "software name"
	return opts, args

def main():
	locale.setlocale(locale.LC_ALL, '')
	opts, args = parse_cmdline()
	apt = Apt(opts)
	apt.run()

if __name__ == '__main__':
	main()