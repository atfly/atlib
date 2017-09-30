
#!usr\bin\env python
# -*- coding: utf-8 -*-
'''
设置JDK的环境变量，基本逻辑：
若已有JAVA_HOME则替换其值，否则创建并添加PATH值
'''
import os
import sys
import optparse

if sys.platform == 'win32':
    import _winreg #使用说明：https://docs.python.org/2/library/_winreg.html#

def configJDK(JDK_Path):
    '''设置JDK的环境变量，输入JDK的安装路径'''
    print("Now:")
    showEnv(["JAVA_HOME","Path","CLASSPATH"])
    print('\n')
    setEnviron("JAVA_HOME",JDK_Path)
    
    BinDir = "%JAVA_HOME%"+os.sep+"bin"
    JreBinDir = "%JAVA_HOME%"+os.sep+"jre"+os.sep+"bin"
    updataEnviron("Path",[BinDir,JreBinDir])
    
    LibDir = "%JAVA_HOME%"+os.sep+"lib"
    LibTools = "%JAVA_HOME%"+os.sep+"lib"+os.sep+"tools.jar"
    updataEnviron("CLASSPATH",[os.curdir,LibDir,LibTools])
    #rebotExplorer()
def setEnviron(Env,Paths):
    print("Set %s = %s" % (Env,Paths))
    if sys.platform == 'win32':
        try:
            EnvironmentKey = _winreg.OpenKey( _winreg.HKEY_CURRENT_USER, r"Environment")
            _winreg.SetValue(EnvironmentKey, Env, _winreg.REG_SZ, Paths)
        except WindowsError:
            "Faile To Control Reg... Are You Administrator?"
            sys.exit()
    else:
        print("Can't Work On your Platform Now!")
        sys.exit()

def getEnviron(Env):
    Paths = ''
    print("Get Environment Variables: %s" % Env)
    if sys.platform == 'win32':
        try:
            EnvironmentKey = _winreg.OpenKey( _winreg.HKEY_CURRENT_USER, r"Environment")
            try:
                Paths, type = _winreg.QueryValueEx(EnvironmentKey, Env)
            except:
                print("There Is No Environment Variables: %s" % Env )
                print("Try To Make It")
                Paths=''
                setEnviron(Env,Paths)
            print("%s = %s " % (Env,Paths) )
        except:
            print("Faile To Control Reg... Are You Administrator?")
            sys.exit()
    else:
        Paths = os.environ.get(Env)
        if Paths == None:
            print("Can't Work On your Platform Now!")
            sys.exit()
    return Paths

def updataEnviron(Env,UpdateList):
    '''用UpdateList的值来更新Env环境变量'''
    print("\nUpdating Environ %s with %s" % (Env,' and '.join(UpdateList) ) )
    OldPaths=getEnviron(Env)
    NewPaths = []
    if OldPaths != '':
        for Path in OldPaths.split(os.pathsep):
            if Path not in UpdateList:
                NewPaths.append(Path)
    NewPaths.extend(UpdateList)
    setEnviron( Env, os.pathsep.join(NewPaths) )

def rebotExplorer():
    os.system("taskkill /im explorer.exe /f")
    os.system("ping -n 2 127.0.0.1 > nul")
    os.system("start c:\windows\explorer.exe")
    import time
    time.sleep(3)

def showEnv(EnvList):
    for Env in EnvList:
        getEnviron( Env)

if __name__ == '__main__':
    configJDK(os.path.abspath(os.curdir))
