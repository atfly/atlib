
#encoding=utf-8

import os

def splitfile(filepath,partialsize=1024*1024*10):

    filedir,name = os.path.split(filepath)

    name,ext = os.path.splitext(name)

    filedir = os.path.join(filedir,name)

    if not os.path.exists(filedir):
        os.mkdir(filedir)
        
    partno = 0
    stream = open(filepath,'rb')

    while True:
        partfilename = os.path.join(filedir,name + '_' + str(partno) + ext)
        print 'write start %s' % partfilename
        part_stream = open(partfilename,'wb')

        read_count = 0
        read_size = 1024*512
        read_count_once = 0

        while read_count < partialsize:
            read_content = stream.read(read_size)
            read_count_once = len(read_content)

            if read_count_once>0:
                part_stream.write(read_content)

            else : break
            
            read_count += read_count_once

        
        part_stream.close()

        if(read_count_once < read_size) : break
        partno += 1

    print 'done'

#www.iplaypy.com
if __name__ == '__main__':
    splitfile(r'E:\quotelogs\quote.data',1024*1024*100)