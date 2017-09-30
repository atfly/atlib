
#-*- coding: UTF-8 -*- 
'''
Created on 2012-3-8

@author: tiantian
www.iplaypy.com python
'''
import urllib
import re

top500 = 'http://list.mp3.baidu.com/top/top500.html'

songs = []

def main():
    
    divr = '<div class="rank-top-wrap clearfix".*?<ul.*?</ul>.*?<ul.*?</ul>.*?</div>'    
    mf = urllib.urlopen(top500)
    content = mf.read()
    content = content.decode('gbk')

    content = re.sub('\n+',' ',content)
    alldiv = re.findall(divr,content)
    i =0
    for div in alldiv:
        ulr = '<ul.*?</ul>'
        allul = re.findall(ulr,div)
        
        for ul in allul:
            lir = '<li.*?</li>'
            allli = re.findall(lir,ul)
            
            for li in allli:
                if i<245:
                    i = i+1
                    continue
                i = i+1
                songName = '<div class="music-name">.*?<a.*?>(.*?)</a>.*?</div>'
                name = re.findall(songName,li)
                songAuthor = '<div class="singer">.*?<a.*?>(.*?)</a>.*?</div>'
                author = re.findall(songAuthor,li)
                
                songs.append([name[0],author[0]])
                
                songUrl = getSongUrl(name[0],author[0])
                try:
                    urllib.urlretrieve(songUrl,'songs/'+name[0]+'-'+author[0]+'.mp3')
                    # 异常检查并不能判断是否下载成功，需要进行其他判断
                    print i,name[0],author[0],'下载成功'
                    
                except Exception :
                    print i,name[0],author[0],'没下载成功'
                    

def getSongUrl(songName,authorName):
	'''这里由于歌曲名称和作者名称的不完整，可能导致无法得到url，'''
    songUrl = 'http://box.zhangmen.baidu.com/x?op=12&count=1&mtype=1&title=%s$$%s$$$$&url=&listenreelect=0&.r=0.1696378872729838' % (urllib.quote(songName.encode('gbk')),urllib.quote(authorName.encode('gbk')))
    f = urllib.urlopen(songUrl)
    c = f.read()
    url1 = re.findall('<encode>.*?CDATA\[(.*?)\]].*?</encode>',c)
    url2 = re.findall('<decode>.*?CDATA\[(.*?)\]].*?</decode>',c)
    if len(url1) <1:
        return 'http://box.zhangmen.baidu.com/unknow.mp3'
    
    try:
        return url1[0][:url1[0].rindex('/')+1] + url2[0]
    except Exception:
        return url1[0]
    
if __name__ == '__main__':
    main()