
import psutil
import re
import sys

#www.iplaypy.com

def processinfo(x):
                    p = psutil.get_process_list()
                    for r in p:
                        aa = str(r)
                        f = re.compile(x,re.I)
                        if f.search(aa):
                    #        print aa.split('pid=')[1].split(',')[0]  
                             print aa.split('pid=')
processinfo(sys.argv[1])

