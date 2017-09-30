
#-*- coding:utf-8 -*-
import base64

#加密程序
def urlencode():
    url=input("\n请输入需要加密的链接地址:").strip()
    print(url)
    thunder="thunder://"+(base64.b64encode(('AA'+url+'ZZ').encode('gb2312'))).decode()
    flashget="[FLASHGET]"+url+"[FLASHGET]"
    flashget="flashget://"+(base64.b64encode(flashget.encode('gb2312'))).decode()+"&abc"
    xuanfeng="qqdl://"+(base64.b64encode(url.encode('gb2312'))).decode()
    print('-'*60)
    print('迅雷加密地址:\n'+thunder+'\n')
    print('快车加密地址:\n'+flashget+'\n')
    print('旋风加密地址:\n'+xuanfeng+'\n')
    over()

#解密程序
def urldecode():
    url=input("\n请输入需要解密的链接地址:").strip()
    url=url.split("://")
    url[0].lower()
    #print(url)
    if url[0]=="thunder":
        deurl=(base64.b64decode(url[1].encode()).decode('gbk'))[2:-2]
        print('解密地址:\n'+deurl+'\n')
        over()

    elif url[0]=="flashget":
        flashurl=(url[1])[:-4]
        print(flashurl)
        deurl=(base64.b64decode(flashurl.encode()).decode('gbk'))[10:-10]
        #deurl=deurl[10:-10]
        print('解密地址:\n'+deurl+'\n')
        over()

    elif url[0]=="qqdl":
        deurl=(base64.b64decode(url[1].encode()).decode('gbk'))
        print('解密地址:\n'+deurl+'\n')
        over()

    elif url[0]=="http" or "ftp" or "https":
        print('你忽悠我呢，解密个啥呢？\n')
        over()

    else:
        print('哥不玩了，蛋疼...\n')
        over()

#www.iplaypy.com
#退出程序
def over():
    input('请输入回车键退出...')
    exit()

#开始执行程序
def acinput():
2966

    print('迅雷+快车+旋风地址加密&解密程序：')
    print('-'*70)
    active=int(input("请选择你要执行的操作:\n1.解密\n2.加密\n3.退出\n输入数字:")[:-1])
    if active==1:
        urldecode()
    elif active==2:
        urlencode()
    elif active==3:
        exit()
    else:
        print('听哥的话还是输个数字吧！')
    acinput()
acinput()
