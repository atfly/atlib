
class JianKong():
    '''查询IDC信息，封ip和过白名单'''
    def __init__(self):
        pass
    @classmethod
    def ip_verify(cls,str):
        '验证IP地址规范'
        pattern=re.compile('(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])')
        s=pattern.findall(str)
        if len(s)>0:
            ip=s[0][0]+'.'+s[0][1]+'.'+s[0][2]+'.'+s[0][3]
            return ip
        else:
            print 'IP格式不正确'#弹窗提醒
            return ''
    @classmethod
    def domain_verify(cls,domainStr):
        '验证域名规范,返回合法域名列表'
        domainList=[]
        file=open('c:\domain.txt','r')
        domainType=file.readlines()
        #去重
        domainType=list(set(domainType))
        #print domainType
        file.close()
        #file=['com','ac','com.cn','net'+'']
        for line in domainType:
            #文件中动态读取每个顶级域名进行匹配
            line=line.strip()
            pattern=re.compile('([a-z0-9][a-z0-9\-]*?\.'+line+')(?:\s|$)+',re.S)
            #例如[a-z0-9][a-z0-9\-]*?\.com.cn(?:\s|$)+ 中(?:\s|$)表示域名后缀后面必须是空白符或者字符结束(?:)表示括号不用于分组功能
            #防止.com.cn先匹配到.com即停止匹配导致错误，或者匹配到.comc多了字符
            result=pattern.findall(domainStr)
            if len(result)>0:
                #正确结果添加到返回列表
                domainList=domainList+result
        #去重
        domainList=list(set(domainList))
        newList=[]
        for d in domainList:
            if d not in domainType and d+'\n' not in domainType:
                newList.append(d)
                    
        return newList
    @classmethod
    def getDomainType(cls):
        '从工信部网站获取所有合法域名后缀'
        file=open('c:/domain.txt','w')
        p=re.compile('class=\"by2\">\.(.*?)\&nbsp;</td>', re.S)
        for i in range(1,23):
            data='domainName=&domainBlur=0&page.pageSize=20&pageNo='+str(i)+'&jumpPageNo='+str(i)
            header={'Host':'www.miitbeian.gov.cn','Origin':'http://www.miitbeian.gov.cn','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 UBrowser/5.5.6125.14 Safari/537.36','Referer':'http://www.miitbeian.gov.cn/basecode/query/queryDomain.action;jsessionid=HSTRWpLZbR0cX4vFkDpnpbNBYyRl4GwW1fxpyhdyc0fcfhkvJTBV!1139295987'}
            url='http://www.miitbeian.gov.cn/basecode/query/queryDomain.action;jsessionid=HSTRWpLZbR0cX4vFkDpnpbNBYyRl4GwW1fxpyhdyc0fcfhkvJTBV!1139295987'
            request=urllib2.Request(url,data,header)
            response=urllib2.urlopen(request)
            recv=response.read()
            s=p.findall(recv)
            #print s
            #去重
            s=list(set(s))
            for y in s:
                file.write(y+'\n')
                file.flush()
                #print str(i)+' '+y
        file.close()
        print '完毕'#弹窗完成