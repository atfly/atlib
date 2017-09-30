
import os,sys,shutil
exclude_dirs = ("include","libs","demo","demos","Tools","__pycache__","test","turtledemo","unittest","pydoc_data","lib2to3")
def rmdir_exclude(root,name):
    if name in exclude_dirs:
        shutil.rmtree(os.path.join(root,name))
        return False
    return True

def walk_dir(path):
    try:
        files = os.listdir(path)
    except:
        print("deny.")
    else:
        for f in files:
            temp = os.path.join(path,f)
            if(os.path.isdir(temp)):
                if rmdir_exclude(path,f):
                    walk_dir(temp)
            else:
                if temp.endswith(".txt") or temp.endswith(".exe") or temp.endswith(".lib") or temp.endswith(".sh"):
                    os.remove(temp)

if __name__ == "__main__":
    walk_dir("d:/PyShell32")//拷贝一份Python3的安装目录