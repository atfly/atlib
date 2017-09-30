
from win32api import *
from win32con import *
from urllib import quote,unquote
def ShowValues(hkey):
i=0
while 1:
try:
name,value,typex=RegEnumValue(hkey,i)
print ” Name :”,name
if typex==1:
type_str=”REG_SZ”
elif typex==2:
type_str=”REG_EXPAND_SZ”
elif typex==3:
type_str==”REG_BINARY”
value=quote(value)
elif typex==4:
type_str=”REG_DWORD”
value=str(value)+’(‘+str(hex(int(value)))+’)’
elif typex==7:#www.iplaypy.com
type_str=”REG_MULTI_SZ”
print ” Value:”,str(value)
print ” Type :”,type_str
print
i+=1
except:
print “=============================”
break
def ShowKeys(root,subkey):
if root==HKEY_CLASSES_ROOT:
rootkey=”HKEY_CLASSES_ROOT\\”
elif root==HKEY_CURRENT_USER:
rootkey=”HKEY_CURRENT_USER\\”
elif root==HKEY_LOCAL_MACHINE:
rootkey=”HKEY_LOCAL_MACHINE\\”
elif root==HKEY_USERS:
rootkey=”HKEY_USERS\\”
print “Path:”,rootkey+subkey
hkey=RegOpenKeyEx(root,subkey,0,KEY_ALL_ACCESS)
ShowValues(hkey)
tuples=RegEnumKeyEx(hkey)
for name,reserved,classx,last in tuples:
ShowKeys(root,subkey+”\\”+name)
def main():
root=HKEY_LOCAL_MACHINE
subkey=”software\\microsoft\\windows\\currentversion\\run”.upper()
ShowKeys(root,subkey)
root=HKEY_CURRENT_USER
ShowKeys(root,subkey)
if __name__==”__main__”:
main()
