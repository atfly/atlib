
import sys, os

if os.name != 'nt':
   print "在windows使用这个模块"
   sys.exit()

try:
   from ctypes import *
except:
   print 'I need module ctypes'
   sys.exit()

try:
   from win32con import *
except:
   print 'I need module win32con'
   sys.exit()

# command colors
cc_map = {
    'default'      :0,
    'black'        :1,
    'blue'         :2,
    'green'        :3,
    'cyan'         :4,
    'red'          :5,
    'magenta'      :6,
    'brown'        :7,
    'lightgray'    :8,
    'darkgray'     :9,
    'lightblue'    :10,
    'lightgreen'   :11,
    'lightcyan'    :12,
    'lightred'     :13,
    'lightmagenta' :14,
    'yellow'       :15,
    'white'        :16,
};
        
CloseHandle = windll.kernel32.CloseHandle
GetStdHandle = windll.kernel32.GetStdHandle
GetConsoleScreenBufferInfo = windll.kernel32.GetConsoleScreenBufferInfo
SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute
#www.iplaypy.com

STD_OUTPUT_HANDLE = -11

class COORD(Structure):
   _fields_ = [('X', c_short),
               ('Y', c_short),
              ]

class SMALL_RECT(Structure):
   _fields_ = [('Left', c_short),
               ('Top', c_short),
               ('Right', c_short),
               ('Bottom', c_short),
              ]
               
class CONSOLE_SCREEN_BUFFER_INFO(Structure):
   _fields_ = [('dwSize', COORD),
               ('dwCursorPosition', COORD),
               ('wAttributes', c_uint),
               ('srWindow', SMALL_RECT),
               ('dwMaximumWindowSize', COORD),
              ]

def print_cc(fore_color, back_color, text):

    if not (cc_map.has_key(fore_color) and
            cc_map.has_key(back_color)):

        #color not found
 
       print >>stderr, fore_color, back_lolor, " are invalid color strings"

        return

    #prepare
    hconsole = GetStdHandle(STD_OUTPUT_HANDLE)
    cmd_info = CONSOLE_SCREEN_BUFFER_INFO()
    GetConsoleScreenBufferInfo(hconsole, byref(cmd_info))
    old_color = cmd_info.wAttributes

    #calculate colors
    fore = cc_map[fore_color]
    if fore: fore = fore - 1
    else: fore = old_color & 0x0F
    back = cc_map[back_color]
    if back: back = (back - 1) << 4
    else: back = old_color & 0xF0

    #real output
    SetConsoleTextAttribute(hconsole, fore + back)
    print text,
    SetConsoleTextAttribute(hconsole, old_color)

if __name__ == "__main__":
    #let's print the color matrix
    #first line
    print("  Color map:")

    keys = [key for key in cc_map]

    for i in range(11, -1, -1): #12 is the max len, "lightmagenta"
        print " " * 20,

        for j in range(0, 17):
            k = keys[j]
            l = len(k)
            c = ' '
            if l > i:
                c = k[l - i - 1]

            print(" %s" % c),

        print

    #lines with color and background cresponding to i & j
  
  for fc in keys:
        print "        %12s " % fc, 

        for bc in keys:

            print_cc(fc, bc, ":)")
        print
