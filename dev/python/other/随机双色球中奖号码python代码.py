
#本代码获取百度乐彩网站上的信息，只获取最近100期的双色球
import urllib.request

from bs4 import BeautifulSoup
import random

ere_hitlist = []
hitlist = []
def getSSQ100():
    site = 'http://trend.lecai.com/ssq/redBaseTrend.action?recentPhase=100&onlyBody=false&phaseOrder=up&coldHotOrder=number'
    page = urllib.request.urlopen(site)
    html = page.read();
    soup = BeautifulSoup(html.decode("utf-8"))
    
    hhlist = soup.find_all("td",class_="red_ball")
    bluelist = soup.find_all("td",class_="blue_ball")
    
    num = 0
    count = 0
    for tag in hhlist:
        global hitlist
        global ere_hitlist
        if num < 6:
            hitlist.append(tag.contents[0])
            if count == 599:
                ere_hitlist.append(hitlist)
                hitlist = []
        elif num == 6 :
            ere_hitlist.append(hitlist)
            hitlist = []
            num = 0
            hitlist.append(tag.contents[0])
        num+=1
        count+=1
    num = 0 
    for sublist in ere_hitlist:
        sublist.append(bluelist[num].contents[0])
        num+=1
        
def chooseSSQ():
    hhlist = []
    lhlist = []
    ylhlist = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33']
    ylllist = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16']
    ylhrlist = []
    yllrlist = []
    num = 0
    for curlist in ere_hitlist:
        for value in curlist:
            num+=1
            for ylval in ylhlist:
                if ylval == value and len(curlist) == num:
                    yllrlist.append(value)
                elif ylval == value and len(curlist) != num:
                    ylhrlist.append(value)
        num = 0
    print("红号：",len(ylhrlist),"蓝号：",len(yllrlist))
    if len(ylhrlist) == 600 and len(yllrlist) == 100:
        lh = random.randint(0,99)
        lhlist.append(ere_hitlist[lh][6])
        
        while len(hhlist) < 6:
            hh = random.randint(0,99)
            hhs = random.randint(0,5)
            hhlist.append(ere_hitlist[hh][hhs])
            hhlist = list(set(hhlist))
        
    elif len(ylhrlist) == 600 and len(yllrlist) != 100:
        lh = random.randint(0,len(yllrlist))
        lhlist.append(yllrlist[lh])
        lh = random.randint(0,15)
        lhlist.append(ylllist[lh])

        while len(hhlist) < 6:
            hh = random.randint(0,99)
            hhs = random.randint(0,5)
            hhlist.append(ere_hitlist[hh][hhs])
            hhlist = list(set(hhlist))
        
    elif len(ylhrlist) != 600 and len(yllrlist) == 100:
        lh = random.randint(0,99)
        lhlist.append(lh)
        
        while len(hhlist) < 3:
            hh = random.randint(0,len(ylhrlist))
            hhlist.append(ylhrlist[hh])
            hhlist = list(set(hhlist))
            
        while len(hhlist) < 6:
            hh = random.randint(0,len(ylhlist))
            hhlist.append(ylhlist[hh])
            hhlist = list(set(hhlist))        

    elif len(ylhrlist) != 600 and len(yllrlist) != 100:
        lh = random.randint(0,len(yllrlist))
        lhlist.append(yllrlist[lh])
        lh = random.randint(0,15)
        lhlist.append(ylllist[lh])
        
        while len(hhlist) < 3:
            hh = random.randint(0,len(ylhrlist))
            hhlist.append(ylhrlist[hh])
            hhlist = list(set(hhlist))
            
        while len(hhlist) < 6:
            hh = random.randint(0,len(ylhlist))
            hhlist.append(ylhlist[hh])
            hhlist = list(set(hhlist))
    
    print("根据前100期双色球中奖号码，本人预测下一期中奖号码是，红号：",hhlist,",蓝号：",lhlist)

if  __name__ == '__main__':
        getSSQ100()
        chooseSSQ()
    