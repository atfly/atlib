
import os
import sys

def Show_file():
    print "lines    filename"
    for i in os.listdir(os.getcwd()):
        if os.path.isfile(i) and not i.startswith("__init__"):
            print os.popen('wc -l %s' % i).read().split('\n')[0]
    print ''

def Query_file():
    filename = raw_input('Input the one filename show above[q to quit]:')
    if filename == 'q':
        sys.exit()

    file = open(filename,'r').readlines()
    print '\n\n'
    for i in file:
        if i.startswith('class') or i.startswith('def') or i.startswith('    def'):
            print i,

#www.iplaypy.com

if __name__ == '__main__':
    Show_file()
    Query_file()