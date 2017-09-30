
import os
import sys

def walk(path) :  

    for filename in os.listdir(path) :
        abspath = path + '\\' + filename

        if os.path.isdir(abspath) :  
            walk(abspath) 

        elif filename.endswith('.cpp') and filename != 'unity_build.cpp' :         
            print '#include "' + abspath[2:] + '"'

sys.stdout = open('./unity_build.cpp', 'w')

walk(os.curdir)

#www.iplaypy.com