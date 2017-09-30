
#!/usr/bin/env python
import os, sys, glob, re

if sys.hexversion < 0x02040000:
        print >> sys.stderr, 'Your python version is too old (%s)' % \
                                                        (sys.version.split()[0])
        print >> sys.stderr, 'You need at least Python 2.4'
        sys.exit(1)

PPATH = False

def search_all_files(pattern, search_path, pathsep=os.pathsep):
    for path in search_path.split(pathsep):
        '''
        candidate = os.path.join(path, filename)
        if os.path.isfile(candidate):
            return os.path.abspath(candidate)
        '''
        for match in glob.glob(os.path.join(path, pattern)):
            yield match

def print_file(pattern, path=None):
    if PPATH:
	p = path.split(' ')
	path = lambda p : os.pathsep.join(p)
	matches = list(search_all_files(pattern, path(p)))
	if matches:
            for match in matches:
                print match
        else:
		print "Not find like '%s' !" % pattern
		sys.exit(1)
    else:
       	matches = list(search_all_files(pattern, os.environ['PATH']))
	if matches:
	    for match in matches:
		print match
	else:
	    print "Not find like '%s' !" % pattern
	    sys.exit(1)

def deep_search(fpattern, path):
	pathlist = path.split(' ')
	finded = False
	for p in pathlist:
		if os.path.exists(p):
			for dirpath, dirnames, filenames in os.walk(p):
				for file in filenames:
					fullpath = os.path.join(dirpath, file)
					if re.search(fpattern, fullpath):
						print fullpath
						finded = True
					else:
						continue
		else:
			print "[*]Path %s don't exit !" % p
			sys.exit(1)
	if not finded:
		print "Don't find like %s !" % fpattern

if __name__ == '__main__':
    if '-p' in sys.argv:
	PPATH = True
	if '-d' not in sys.argv:
		if len(sys.argv) != 4 or sys.argv[1].startswith('-'):
	    		print "Usage %s <pattern> -p 'path1 path2 path3....' use escape to split pathname" % sys.argv[0]
		else:
	    		print_file(sys.argv[1], sys.argv[3])
	elif sys.argv[4] == '-d':
		deep_search(sys.argv[1], sys.argv[3])
    else:
	if len(sys.argv) != 2 or sys.argv[1].startswith('-'):
		print "Usage %s <pattern> " % sys.argv[0]
		sys.exit(1)
        else:
            print_file(sys.argv[1])
