
from ctypes import *

kernel32 = windll.kernel32
#定义数据结构中的字段类型

WORD      = c_ushort
DWORD     = c_ulong
LPBYTE    = POINTER(c_ubyte)
LPTSTR    = POINTER(c_char)
HANDLE    = c_void_p
#定义函数中的初始化变量值

CREATE_NEW_CONSOLE    = 0x00000010
PROCESS_ALL_ACCESS    = 0x001F0FFF
INFINITE              = 0xFFFFFFFF

#STARTUPINFO数据结构

class STARTUPINFO(Structure):
    _fields_ = [
        ("cb",            DWORD),       
        ("lpReserved",    LPTSTR),
        ("lpDesktop",     LPTSTR), 
        ("lpTitle",       LPTSTR),
        ("dwX",           DWORD),
        ("dwY",           DWORD),
        ("dwXSize",       DWORD),
        ("dwYSize",       DWORD),
        ("dwXCountChars", DWORD),
        ("dwYCountChars", DWORD),
        ("dwFillAttribute",DWORD),
        ("dwFlags",       DWORD),
        ("wShowWindow",   WORD),
        ("cbReserved2",   WORD),
        ("lpReserved2",   LPBYTE),
        ("hStdInput",     HANDLE),
        ("hStdOutput",    HANDLE),
        ("hStdError",     HANDLE),
        ]

#PROCESS_INFORMATION数据结构
class PROCESS_INFORMATION(Structure):
    _fields_ = [
        ("hProcess",    HANDLE),
        ("hThread",     HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId",  DWORD),
        ]
 
#www.iplaypy.com

class debugger():
    def __init__(self):
        #pass
        self.h_process = None
        self.pid = None
        self.debugger_active = False

    def load(self,path_to_exe):

        #实例化上述两个数据结构，并设置标志，这里是现实在桌面上（也可以隐藏，因设置的标志不同而不同）
        creation_flags = CREATE_NEW_CONSOLE
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0
        startupinfo.cb = sizeof(startupinfo)
        #调用win32中的函数CreateProcessA打开所给应用程序

        if kernel32.CreateProcessA(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   None,
                                   creation_flags,
                                   None,
                                   None,
                                   byref(startupinfo),
                                   byref(process_information)):
            print "[*] We have successfully launched the process!"
            print "[*] PID: %d" % process_information.dwProcessId
        else:
            print "[*] Error: 0xx." % kernel32.GetLastError()
        #return process_information.dwProcessId

if __name__ == "__main__":
    debugger = debugger()
    debugger.load("C:\\WINDOWS\\system32\\calc.exe")
