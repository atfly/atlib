
#!/usr/bin/env pyton
# _*_ coding: gbk _*_

from sys import argv, exit, stdout, stdin
from os import path, isatty
from getopt import getopt, GetoptError

help_info = ["more.py [-h] file list...",
		"\t-h\t显示帮助信息"]

class _Getch:
	"""Gets a single character from standard input.  Does not echo to the screen."""
	def __init__(self):
		try:
			self.impl = _GetchWindows()
		except ImportError, err:
			self.impl = _GetchUnix()

	def __call__(self): return self.impl()

class _GetchUnix:
	def __init__(self):
		import tty, sys

	def __call__(self):
		import sys, tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

class _GetchWindows:
	def __init__(self):
		import msvcrt

	def __call__(self):
		import msvcrt
		return msvcrt.getch()

getch = _Getch()

def usage():
	for l in help_info:
		print l

def do_more(lines):	
	num_of_lines = 0		
	i = 0
	while i < len(lines):
		num_of_lines = num_of_lines + 1 
		stdout.write(lines[i])
		i += 1
		if num_of_lines >= 12:
			num_of_lines = see_more(num_of_lines)
		if num_of_lines < 0:
			i += num_of_lines
		if i < 0:
			i = 0

def see_more(num_of_lines):
	answer = getch()
	if answer== " ":
		return 0
	elif answer == "\r":
		return (num_of_lines - 1)
	elif answer == "q":
			exit(1) 
	elif answer == "b":
		return (-num_of_lines)	
	else:
		return 0


if __name__ == "__main__":
	try:
		opts, args = getopt(argv[1:], "h")				
	except GetoptError, err:
		print str(err)
		usage()
		exit(2)
	for o, a in opts:
		if o == "-h":
			usage()
			exit(0)	
		else:
			print "Unkown options"
			usage()
			exit(2)
	if len(args) == 0:
		usage()

#www.iplaypy.com

	else:
		for file in args:
			if not path.exists(file):
				print file + ": No such file or directory"
			else:
				print file + ":"
				fp = open(file, 'r')
				lines = fp.readlines()
				do_more(lines)
