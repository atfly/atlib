
# coding: utf-8

import win32gui
import win32process
import win32con
import win32api
from ctypes import *

#雷区最大行列数
MAX_ROWS = 24
MAX_COLUMNS = 30

#雷区格子在窗体上的起始坐标及每个格子的宽度
MINE_BEGIN_X = 0xC
MINE_BEGIN_Y = 0x37
MINE_GRID_WIDTH = 0x10
MINE_GRID_HEIGHT = 0x10

#边框、无雷、有雷的内部表示
MINE_BOARDER = 0x10
MINE_SAFE = 0x0F
MINE_DANGER = 0x8F

#“雷区”在 扫雷程序中的存储地址
BOARD_ADDR = 0x1005340

class SMineCtrl(Structure):
    _fields_ = [("hWnd", c_uint),
                ("board", (c_byte * (MAX_COLUMNS + 2)) * (MAX_ROWS + 2)),
                ("rows", c_byte),
                ("columns", c_byte)
        ]

kernel32 = windll.LoadLibrary("kernel32.dll")

ReadProcessMemory = kernel32.ReadProcessMemory

WriteProcessMemory = kernel32.WriteProcessMemory

OpenProcess = kernel32.OpenProcess
ctrlData = SMineCtrl()

#找到扫雷程序并打开对应进程
try:
    ctrlData.hWnd = win32gui.FindWindow("扫雷", "扫雷")

except:
    win32api.MessageBox(0, "请先运行扫雷程序", "错误！", win32con.MB_ICONERROR)
    exit(0)

hreadID, processID = win32process.GetWindowThreadProcessId(ctrlData.hWnd)

hProc = OpenProcess(win32con.PROCESS_ALL_ACCESS, 0, processID)

#读取雷区数据
bytesRead = c_ulong(0)

ReadProcessMemory(hProc, BOARD_ADDR, byref(ctrlData.board), SMineCtrl.board.size, byref(bytesRead))

if(bytesRead.value != SMineCtrl.board.size):
    str =  "ReadProcessMemory error, only read ", bytesRead.value, " should read ", SMineCtrl.board.size
    win32api.MessageBox(0, str, "错误！", win32con.MB_ICONERROR)
    exit()

#www.iplaypy.com

#获取本次程序雷区的实际大小
ctrlData.rows = 0

ctrlData.columns = 0

for i in range(0, MAX_COLUMNS + 2):
    if MINE_BOARDER == ctrlData.board[0]:
        ctrlData.columns += 1
    else :
        break

ctrlData.columns -= 2   

for i in range(1, MAX_ROWS + 1):
    if MINE_BOARDER != ctrlData.board[1]:
        ctrlData.rows += 1
    else:
        break

#模拟鼠标点击动作
for i in range(0, ctrlData.rows):

    for j in range(0, ctrlData.columns):

        if MINE_SAFE == ctrlData.board[i + 1][j + 1]:
                win32api.SendMessage(ctrlData.hWnd,
                                     win32con.WM_LBUTTONDOWN,
                                     win32con.MK_LBUTTON,
                                     win32api.MAKELONG(MINE_BEGIN_X + MINE_GRID_WIDTH * j + MINE_GRID_WIDTH / 2,
                                                       MINE_BEGIN_Y + MINE_GRID_HEIGHT * i + MINE_GRID_HEIGHT / 2))
                win32api.SendMessage(ctrlData.hWnd,
                                     win32con.WM_LBUTTONUP,

win32con.MK_LBUTTON,
                                     win32api.MAKELONG(MINE_BEGIN_X + MINE_GRID_WIDTH * j + MINE_GRID_WIDTH / 2,
                                                       MINE_BEGIN_Y + MINE_GRID_HEIGHT * i + MINE_GRID_HEIGHT / 2))

#完成任务
win32api.MessageBox(0, "搞定！", "信息", win32con.MB_ICONINFORMATION)