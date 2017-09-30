
#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import re
import shutil

start_re = re.compile(r'^#<--\s*((?:\d){,4}-(?:\d){,2}-(?:\d){,2})')

java_re = re.compile(r'\.java$')
end_tag = r'#-->'
cur_path = os.getcwd()
file = open(os.path.join(os.getcwd(), 'changelog.txt'), 'r')
src_basic_dir = os.getcwd()
dest_basic_dir = os.path.join(os.getcwd(), 'deploy')

deploy_version = None
isend = False
deploy_files = []
#www.iplaypy.com

try:
	for l in file:
		l = l.strip()
		if not deploy_version:
			m = re.search(start_re, l)
			if m:
				deploy_version = m.group(1)

				if deploy_version:
					dest_basic_dir = os.path.join(dest_basic_dir, deploy_version.replace('-',''))
					continue
			
		if l == end_tag:
			isend = True
			break

		if not isend:
			deploy_files.append(l)

	for f in deploy_files:
		f = f.replace('\\', '/')
		
		if f.startswith(r'src/'):
			
			f = re.sub(re.compile(r'^src/'), r'build/', f)
			f = re.sub(java_re, '.class', f)
			src_file = os.path.join(src_basic_dir, f).replace('\\', '/')
			dest_file = os.path.join(dest_basic_dir, re.sub(re.compile(r'^build/'), r'WEB-INF/classes/', f)).replace('\\', '/')
		else:
			src_file = os.path.join(src_basic_dir, f).replace('\\', '/')
			dest_file = os.path.join(dest_basic_dir, re.sub(re.compile(r'^(\w+?)/'), '', f) ).replace('\\', '/')
		
		dest_dir = os.path.dirname(dest_file)
		if not os.path.exists(dest_dir):
			os.makedirs(dest_dir)
		if not os.path.isfile(dest_file):
			print src_file + " --> " + dest_file + "----------new"
		else:
			print src_file + " --> " + dest_file + "----------overwrite"
		print "=============================="
		shutil.copy2(src_file, dest_file)
	sys.exit(-1)

except KeyboardInterrupt:
	print '~ ...'

    sys.exit(0)