
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import  urllib2, sys, os, getopt
def usage():
    print """用法: getip [选项]... [ip或域名]...[ip或域名]...
查询IP或域名对应IP信息，可同时查询一个或多个。
不接任何参数将返回本机IP信息。
选项说明：
-h, --help                返回本帮助信息
-i, --infile=filepath        从文件中读取IP，文件格式每行一个IP或域名
例:getip 192.168.0.1 [url]www.xnlinux.cn[/url]
   getip -i ip.txt
发现任何问题请向[email]itxx00@gmail.com[/email]报告。"""
def printip(ip): #打印IP信息
    type = sys.getfilesystemencoding()
    encodeip = ip.decode("GBK").encode(type)
    resultip = encodeip.split(">")
    ip = (resultip[1]).split("<")[0]
    location = (resultip[2]).split("：")[1]
    print ip,location
def main():
    try: #获取命令行参数
        opts,args = getopt.getopt(sys.argv[1:],"hi:",["help","infile="])
    except getopt.GetoptError: #参数错误处理
        usage()
        sys.exit()
    if len(sys.argv) == 1: #未加参数则显示本机IP信息
        localip = urllib2.urlopen("http://ip.cn/getip.php?action=getip").read()
        print "本机IP:",
        printip(localip)
        sys.exit()
    for o,a in opts: #接受参数选项
        if o in ("-h","--help"): #帮助信息
            usage()
            sys.exit()
        if o in ("-i","--infile"): #从文件读取查询的IP
            if os.path.isfile(a):
                file = open(a,"r")
                for fip in file:
                    queryip = urllib2.urlopen("http://ip.cn/getip.php?action=queryip&ip_url="+fip).read()
                    printip(queryip)
                file.close()
            else:
                print "文件",a,"不存在"
                sys.exit()
    else: #从命令行参数获取查询的IP
        for i in args:
            queryip = urllib2.urlopen("http://ip.cn/getip.php?action=queryip&ip_url="+i).read()
            printip(queryip)
if __name__ == "__main__":
    main()
