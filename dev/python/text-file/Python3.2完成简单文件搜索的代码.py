
import os
import time
import re
import threading

class brid:
    def __init__(self):
        th=threading.Thread(target=self.dt(),args="")
        th.start()
        threading.Thread.join(th)
        pass

    def dt(self):
        a=True
        while a is True:
            print("xx")
            time.sleep(3)
            a=False

    def FileSearch(self,keywords,path):
        print("searching...")
        results=[]
        i=0
        j=0

        time_start=time.time()

        for root,dirs,filenames in os.walk(path):
            for file in filenames:
                i=i+1
                if re.search(keywords,file):
                    j=j+1
                    filef=os.path.join(root,file)
                    print(filef)
                    results.append(filef)

        time_end=time.time()
        time_used=time_end-time_start
        print("符合的文件 : ",j)
        print("共扫描文件 : ",i)
        print("花费时间 : ",time_used)
        return results

    def FileSearchEx(self):
        keywords=input("the keywords : ")
        path=input("target dir : ")
        destination=input("the results : ")
        print("searching...")
        results=[]
        i=0
        j=0
        time_start=time.time()

        for root,dirs,filenames in os.walk(path):
            for file in filenames:
                i=i+1
                if re.search(keywords,file):
                    j=j+1
                    filef=os.path.join(root,file)
                    results.append(filef)

        time_end=time.time()
        time_used=time_end-time_start
        fh=open(destination,"w+")
        for t in results:
            fh.write("\n"+t)
        fh.write("\n符合的文件 : "+str(j))
        fh.write("\n共扫描文件 : "+str(i))
        fh.write("\n花费时间 : "+str(time_used))
        fh.close()
        os.system(destination)
        return results
        #www.iplaypy.com

if __name__=="__main__":
    yz=brid()
    yz.FileSearchEx()
            
