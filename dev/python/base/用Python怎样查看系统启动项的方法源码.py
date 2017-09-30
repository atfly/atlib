
1.#-*- coding: UTF-8 -*-    

3.import string                           
4.# 导入所需要的模块   
5.from win32api import *   
6.from win32con import *   
7.def GetValues(fullname):       
8.#  GetValues函数用于获得某注册表项下所有的项值   
9.  name=string.split(fullname, '\\', 1)    
10.#  把完整的项拆分成根项和子项两部分   
11.# 打开相应的项，为了让该函数更通用   
12.# 使用了多个判断语句   
13.  if name[0] == 'HKEY_LOCAL_MACHINE':   
14.    key = RegOpenKey(HKEY_LOCAL_MACHINE, name[1], 0, KEY_READ)   
15.    elif name[0] == 'HKEY_CURRENT_USER':   
16.        key = RegOpenKey(HKEY_CURRENT_USER, name[1], 0, KEY_READ)   
17.        elif name[0] == 'HKEY_CLASSES_ROOT':   
18.            key = RegOpenKey(HKEY_CLASSES_ROOT, name[1], 0, KEY_READ)   
19.            elif name[0] == 'HKEY_CURRENT_CONFIG':   
20.                key = RegOpenKey(HKEY_CURRENT_CONFIG, name[1], 0, KEY_READ)   
21.                elif name[0] == 'HKEY_USERS':   
22.                    key = RegOpenKey(HKEY_USERS, name[1], 0, KEY_READ)   
23.                    else:   
24.                        print 'err,no key named %s' (name[0])  info = RegQueryInfoKey(key)        
25.                         # 查询项的项值数目   
26.                         # 遍历项值获得项值数据   
27.                         for i in range(0, info[1]):   
28.                             ValueName = RegEnumValue(key, i)   
29.                             print string.ljust(ValueName[0], 20), ValueName[1]    
30.                             # 调整项值名称长度，使输出更好看RegCloseKey(key)                    
31.                             # 关闭打开的项# 因为GetValues函数比较通用，所以可以在其他脚本中调用   
32.                             # 这里先检查脚本是否被其他脚本调用          
33.                             if _name_ == '_main_':    
34.                               # 因为要检查的项较多，故将其放在列表中，便于增减     
35. #www.iplaypy.com          KeyNames = ['HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion
                                      \\Run', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\
                                      CurrentVersion\\  RunOnce', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\
                                      Microsoft\\Windows\\CurrentVersion\\  RunOnceEx', 
                                      'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion
                                       \\Run', 'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\
                                        CurrentVersion\\  RunOnce']   
36.                                 for KeyName in KeyNames:                           
37.                                     # 遍历列表，调用GetValues函数， 输出项值   
38.                                     print KeyName   
39.                                     GetValues(KeyName)   
