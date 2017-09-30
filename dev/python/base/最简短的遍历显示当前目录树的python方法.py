
from os.path import basename, isdir
from os import listdir

def traverse(path, depth=0):
    print depth* '| ' + '|_', basename(path)
    if(isdir(path)):
        for item in listdir(path):
            traverse(path+'/'+item, depth+1)

if __name__ == '__main__':
    traverse('./')