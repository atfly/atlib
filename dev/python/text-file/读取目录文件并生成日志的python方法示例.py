
    import os  
    from time import strftime  

    stamp=strftime("%Y-%m-%d %H:%M:%S")  

    logfile = 'F://test//m-php-framework//tmp/logs//error_report.log'  

    path = 'F://test//'  

    files = os.listdir(path)  

    bytes = 0  

    numfiles = 0  

    for f in files: #www.iplaypy.com 
        if f.startswith('t'):  
            info = os.stat(path + f)  
            numfiles +=1  
            bytes+=info[6]  

    if numfiles > 1:  
        title = 'tiles'  

    else:  
        title = 'file'  

    string = stamp + " -- " + str(numfiles) + " session" +title+","+ str(bytes)+" bytes/n"  

    file = open(logfile,"a")  

    file.writelines(string)  

    file.close()  