
#! /usr/bin/python   

# -*- coding: utf-8 -*-   

import urllib,re,unicodedata,string,sys   
from time import strftime,localtime   

channel={"1":"CCTV-1","2":"CCTV-2","3":"CCTV-3","4":"CCTV-4亚洲",   
        "5":"CCTV-4欧洲","6":"CCTV-4美洲","7":"CCTV-5","8":"CCTV-6",   
        "9":"CCTV-7","10":"CCTV-8","11":"CCTV-9","12":"CCTV-10",   
        "13":"CCTV-11","14":"CCTV-12","15":"CCTV新闻","16":"CCTV少儿",   
        "17":"CCTV音乐","18":"CCTV_E","19":"CCTV-F","20":"CCTV-高清"}   

if __name__=="__main__":   
        print "@@"  
        print "@@ 你可以在命令行后输入数字(1-20)来选择频道 "  
        print "@@ 通过在命令行后键入help获取频道列表"  
        print "@@"  
        if len(sys.argv)==1:   
                Select="8"  
        else:   
                if sys.argv[1]=="help":   
                        for i in range(len(channel)):   
                                print "%3d : %11s" % (i+1, channel["%s" % (i+1)]),   
                                if(i%4 == 3):   
                                        print ""   
                        sys.exit(0)   
                if string.atoi(sys.argv[1])>20 or string.atoi(sys.argv[1])<=0:   
                        print "Out of Range. Please Select 1-20."  
                        sys.exit(0)   
                else:   
                        Select=sys.argv[1]   
        print '正在获取节目单，请稍后...'  
        date=strftime('%Y%m%d',localtime())   
        response = urllib.urlopen("http://tv.cctv.com/soushi/28/0"+Select+"/"+date+".shtml")   
        Result=response.read()   
        #list=re.findall(r"<div class='tlb_right'><div class='l'>(.+?)<script",Result,re.S)   
        list=re.findall(r"上午节目(.+?)<script",Result,re.S)   
        list2=re.findall(r"<li>(.+?)</li>",list[0],re.S)   
        morning=[]   
        afternoon=[]   
        listnum=0  

        for i in range(len(list2)):   
                i=re.sub('<.+?>','',list2[i])   
                if string.atoi(i[:2])>=12:  #将上午的节目于下午的节目分开   
                        afternoon.append(i)   
                else:   
                        morning.append(i)   
        if len(morning)>len(afternoon):   
                listnum=len(morning)   
        else:   
                listnum=len(afternoon)   
        print "-"*80,   
        print " "*13+"上午节目"+" "*26+"下午节目"  
        print " "*14+"========"+" "*26+"========"  
#www.iplaypy.com
        for i in range(listnum):   
                if(i<len(morning)):   
                        print "%-4s %-29s" %(morning[i][:5],morning[i][5:]),   
                else:   
                        print " "*35,   
                if(i<len(afternoon)):   
                        print "%-4s %-30s" %(afternoon[i][:5],afternoon[i][5:])   
                else:   
                        print " "*37  
        print "-"*80,   
        print " "*24,strftime("%Y年%m月%d日"),   
        print "%s 节目单" %channel[Select] 
