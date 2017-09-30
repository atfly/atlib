

#! /usr/bin/env python
# -*- coding: utf-8 -*-
#以上为解释器路径及编码声音

#以下导入方法模块
import struct
import _winreg
import sys

#proxy = sys.argv[1]
#www.iplaypy.com

proxy = "127.0.0.1:8118"

root = _winreg.HKEY_CURRENT_USER

proxy_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"

kv_Enable = [
  (proxy_path, "ProxyEnable", 1, _winreg.REG_DWORD),
  (proxy_path, "ProxyServer", proxy, _winreg.REG_SZ),
]

kv_Disable = [
  (proxy_path, "ProxyEnable", 0, _winreg.REG_DWORD),
  (proxy_path, "ProxyServer", proxy, _winreg.REG_SZ),
]

hKey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, proxy_path)
value, type = _winreg.QueryValueEx(hKey, "ProxyEnable")

kv = kv_Enable

result = "Enabled"

if value:
    result = "Disabled"
    kv = kv_Disable

for keypath, value_name, value, value_type in kv:
    hKey = _winreg.CreateKey (root, keypath)
    _winreg.SetValueEx (hKey, value_name, 0, value_type, value)

print result

