
# To change this template, choose Tools | Templates
# and open the template in the editor.

# coding=utf-8

import os
import sys
import xml.dom.minidom 

__author__="Administrator"
__date__ ="$2011-9-4 6:10:46$"


def main(args):
#    print(args)
    dom = xml.dom.minidom.parse('default.xml') 
    root = dom.documentElement 
    for node in root.getElementsByTagName('project'): 
       names = node.getAttribute("name")
       paths = node.getAttribute("path")
       
       namedirs = names.split('/')
       print(namedirs)
       
       os.system("cd ..")
       
       newdir = ''
       for ndir in namedirs[:-1]:
           newdir += ndir + '/';
       print(newdir)
       command = newdir
       try:
        os.makedirs (command)#创建存在的目录会出错 懒得判断了 
       except:
           print('great! im an error')
           #www.iplaypy.com    
    
       command = "cd " + newdir + " && " + "git clone git://git.omapzoom.org/" + names + ".git -b froyo"
       print(command)
       os.system(command)

if __name__ == '__main__':
    main(sys.argv[1:])
