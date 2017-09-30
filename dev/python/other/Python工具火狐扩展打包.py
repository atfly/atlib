
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# packaging of firefox add-on and studing python
#
# usage: put this file to addon folder. 
#		 double click or running in the shell 
# last edited: Dec. 2011

from shutil import ignore_patterns, rmtree ,copytree
import os, tempfile, os.path as osp,re, zipfile

def packaging(src):
	"""
		reading install.rdf and packaging a xpi file. 
		for example: 
			xxx-0.1.xpi
	"""
	work_copy = osp.dirname(src)
	
	addon_info = "".join(open(work_copy + osp.sep + "install.rdf"))
	addon_name = re.search("(?<=em\:name\=\").*(?=\")",addon_info).group(0)
	addon_version =  re.search("(?<=em\:version\=\").*(?=\")",addon_info).group(0)

	temp_copy_base = tempfile.mkdtemp()
	temp_copy = osp.join(temp_copy_base,addon_name)
	
	xpi_name = "%s-%s.xpi" % (addon_name,addon_version)
	xpi_fullpath = osp.join(work_copy,xpi_name);
	
	print """
	Add-on    : %s
	Version   : %s
	Work Copy : %s
	Temp Copy : %s
	XPI File  : %s
	""" % (addon_name,addon_version,work_copy,temp_copy, xpi_name)

	print "copying work to temp dir..."
	copytree(work_copy,temp_copy,ignore=ignore_patterns('*.xpi','.*','*.bat','*.py','*LOG','*~','*.swp'))

	print "packaging xpi..."
	compress(temp_copy,xpi_fullpath);

	print "cleaning..."
	rmtree(temp_copy_base)

#www.iplaypy.com
def compress(src,dstfile):
	"""
		compressing src to dstfile
	"""
	afile = zipfile.ZipFile(dstfile,"w",zipfile.ZIP_DEFLATED)
	for root,dirs,files in os.walk(src):
		for filename in files:
			abspath = osp.join(root,filename)
			relpath = osp.relpath(abspath,src)
			afile.write(abspath, relpath)


if __name__ == "__main__":
	packaging(__file__)