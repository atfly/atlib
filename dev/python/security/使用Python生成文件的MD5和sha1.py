
#coding=UTF-8
# www.iplaypy.com python
# XingHe Studio File to MD5 and SHA1

def fil_changefileext(filename,extname=''):
    # FIL ChangeFileExt 改变文件扩展名
    # filename    输入的文件路径名
    # extname=''  要更改分扩展名，如 .txt
    import os
    try:
        if extname[0]<>'.':
            extname='.'+extname
    except:
        extname=''
    if os.path.splitext(filename)[1]=='':
        uouttxt=filename+'.'+extname
    elif os.path.splitext(filename)[1]=='.':
        uouttxt=filename+extname    
    else:
        uouttxt=filename[:0-len(os.path.splitext(filename)[1])]+extname
    return uouttxt

def fil_str2file(fstr,filename):
    # FIL STR2File 把字符串保存到文件 
    try:
        outfile=open(filename,'w')
        outfile.writelines(fstr)
        outfile.close()
        return True    
    except:
        return False
    
#系统主程序开始
#-------------------------------------------------------
if __name__ == '__main__':    
    import os,sys,math
    # if len(sys.argv)==1:sys.argv.append(r'c:\FreeNAS-8.0.4-RELEASE-x64.iso')
    if len(sys.argv)>1:
        filepathname=sys.argv[1]
        if os.path.isfile(filepathname) :
            fmaxs = os.path.getsize(filepathname)+0.00
            fpos = 0.00
            ppos=0  
            pmax=50
            pjy=0          
            fmd5=fil_changefileext(filepathname,'.md5')
            fsha1=fil_changefileext(filepathname,'.sha')
            ffm=os.path.basename(filepathname)            
            #开始处理
            print 'Program Runing "'+filepathname+'" ...'
            import hashlib
            try:
                umd5str = hashlib.md5()
                usha1str = hashlib.sha1()
                xfilepathname=unicode(filepathname,'utf8')
                #需要使用二进制格式读取文件内容
                ufile = file(xfilepathname,'rb')
                while True:
                    datas = ufile.read(1024*512)
                    if not datas: break
                    umd5str.update( datas )
                    usha1str.update( datas )
                    fpos=fpos+1024*512
                    ppos=int(math.floor(fpos / fmaxs * 50))
                    pposbfh=int(math.floor(fpos / fmaxs * 100))
                    #打印进度条
                    if pjy<>ppos: print '['+'*'*ppos +'='*(pmax-ppos)+'] '+str(pposbfh) +'%'
                    #打印进度问题未解决，不知道print函数怎么退回到行首覆盖输出，不换行我倒是知道，加个“,”  
                    pjy=ppos 
                uoutstrmd5=str(umd5str.hexdigest())
                uoutstrsha1=str(usha1str.hexdigest())
                ufile.close()
                print ''
                fil_str2file(uoutstrmd5+' *'+ffm+'\n',fmd5)
                fil_str2file(uoutstrsha1+' *'+ffm+'\n',fsha1)
                print 'Task is completed !' + r' [ XingHe Studio File to MD5 and SHA1 ]'                
            except:        
                print 'Error !' + r' [ XingHe Studio File to MD5 and SHA1 ]'
        else:
            print 'File "'+filepathname+'" not exist!'+ r' [ XingHe Studio File to MD5 and SHA1 ]'
    else:
        print  r' [ XingHe Studio File to MD5 and SHA1 ]'
        
