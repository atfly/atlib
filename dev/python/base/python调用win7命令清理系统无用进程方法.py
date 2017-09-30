

# -*- coding: cp936 -*-
import os,string
import re
#coding=utf-8

# re rule,to search process PID
rule = re.compile('\s\d+\s')

#www.iplaypy.com

# Get the Message of the all running process and PID  
ProcMessage = os.popen('tasklist').readlines()

# Process list to be killed
KillProclist = ['PPLiveU.exe',
                'wireshark.exe',
                'BitCometService.exe',
                'BitComet.exe',
                'FTPServer.exe',
                'QvodTerminal.exe',
                'PPLive.exe',
                'PPStream.exe',
                'Uedit32.exe',
                'PPSAP.exe',
                'emule.exe',
                'QvodPlayer.exe',
                'wireshark.exe ',
                'SogouCloud.exe',
                'PPAP.exe',
                'AcroRd32.exe' ,
                'firefox.exe',
                'dwm.exe',
                'IcbcDaemon.exe',]

#Store the process name : PID
table={}

def SearchPID(temp):  # To search process PID by Name
    '''Find Proccess Name,Return PID'''
    print 'Proc Name     status     PID'
    for eachline in ProcMessage: # Get a list of running process message to match
        for sub in temp:
            if eachline.find(sub)==0: # if 0 ,Find the process to be killed
                ret = re.search(rule,eachline) # Get the PID
                if ret is not None:
                    print sub,'  running  ',ret.group(0)
                    table.update({sub:ret.group(0)}) # Add {process name:PID} to the Table list
   # print table
    if table == {}:
        print 'No useless process is running!'
    return table

def KillPID(temp):
    for key in temp.keys():
        # Use system cmd TaskKill /T   终止指定的进程和由它启用的子进程
        #                         /F   强制终止
        #                         /IM  指定终止进程的映像名称
        #                         /PID 指定要终止进程的PID
        cmd='TaskKill /T /F /PID %s' % (temp[key]) 
        #print '进程名称:',key
        os.popen(cmd)       # carry out the cmd
        print  'Kill process [',key,'] Successful!'        
       
if __name__=='__main__':
    
   SearchRet=SearchPID(KillProclist)
   
   KillPID(SearchRet)
                        
