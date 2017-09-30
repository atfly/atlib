
import os

def delete_file_folder(src):
    '''delete files and folders'''

    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass

#www.iplaypy.com

    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc=os.path.join(src,item)
            delete_file_folder(itemsrc) 
        try:
            os.rmdir(src)
        except:
            pass

if __name__=='__main__':

    dirname=r'G:\windows'

    print delete_file_folder(dirname)

