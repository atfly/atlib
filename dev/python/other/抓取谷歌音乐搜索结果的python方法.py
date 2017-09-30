
#! /usr/bin/env python
#coding=utf-8

'''
Created on 2011-8-19

'''

from urllib import request,parse
import re,sys

def extractSongRawData(text):
    '抓取每一首歌的原始数据'
    text = re.sub('\n+','',text)
    songList = re.findall('\<tbody.*?\</tbody>',text)
    nums = len(songList)
    print('search ' + str(nums) + ' songs')
    return songList

def translate(text):
    '去掉text中的无用字符，转换unicode码'
    text = re.sub('\<b>','',text)
    text = re.sub('\</b>','',text)
    
    #find the &#25104; and translate into chinese
    s = re.findall('&#([0-9]+);',text)

    if len(s)<=0:
        return text
    else:
        text = ''
        for i in range(len(s)):
            value = int(s[i],10) #from str'123' to 10 base's int 124
            text += chr(value)   #from value to char
            
        return text
    
def extractSongName(song):
    '提取歌曲名字'
    td = re.findall('(?:\<td class\="Title).*(?:\</td>)',song)
    name = re.findall('.+?\<a.+?>(.*?)\</a>',td[0])
    
    songName = translate(name[0])
    return songName

def extractAuthorName(song):
    '提取作者名字'
    td = re.findall('(?:\<td class\="Artist).*(?:\</td>)',song)
    name = re.findall('.+?\<a.+?>(.*?)\</a>',td[0])
    authorName = name[0]
    
    authorName = translate(authorName)
    return authorName

def extrackAlbumName(song):
    '提取专辑名字'
    td = re.findall('(?:\<td class\="Album).*(?:\</td>)',song)
    name = re.findall('.+?\<a.+?>(.*?)\</a>',td[0])
    
    albumName = translate(name[0])
    return albumName

def extractID(song):
    '提取歌曲id'
    td = re.findall('''\<tbody id\="([a-zA-Z0-9]+)"''',song)
    if len(td)>0:
        return td[0]
    else:
        return song
  
def extractLink(song):
    '提取歌曲下载链接'
    td = re.findall('''\<td class\="Icon.*?(?=title\="下载").*?onclick\="(.*?)>''',song)
    if len(td) == 0:
        return 'NULL'
    s = str(td[0])
    rawLink = re.findall('http.*?(?=\?)',s)
    if len(rawLink) == 0:
        return s
    
    link = rawLink[0]
    link = re.sub('%3D','=',link)
    id = extractID(song)
    return link + '?id=' + id

def extractPageNums(text):
    '提取返回结果的页数，最多要10页'
    pageList = re.findall('page_link',text)
    return len(pageList)

def extractSongInfo(song):
    '提取歌曲信息，返回歌曲列表'
    songList = []
    for i in range(len(song)):
        songName = extractSongName(song[i])
        authorName = extractAuthorName(song[i])
        albumName = extrackAlbumName(song[i])
        link = extractLink(song[i])
        
        songItem = [songName,authorName,albumName,link]
        songList.append(songItem)
        
        index = ''
        if i<9:
            index = '0' + str(i+1)
        else:
            index = str(i + 
1c40
1)
        #print(index + '  ' + songName + '  ' + authorName + '  ' + albumName + '  ' + link)
        
    return songList
    
def main():
    while True:
        url = 'http://www.google.cn/music/search?q='
        key = input('请输入歌曲名字或关键字:')
    
        key = parse.quote(key) #统一编码成utf-8
        url += key
        
        mf = request.urlopen(url)
        c = mf.readall()
        c = str(c,encoding = 'utf-8')
        
        num = extractPageNums(c)
        print(str(num+1) + ' pages found')
        
        song = extractSongRawData(c)
        songList = extractSongInfo(song)
        
        #if the result great than 2 pages, then request all pages
        if num>0:

            for i in range(num):
                start = (i+1)*20
                next_page = '&cat=song&start=%d'%(start)
                #next_page = parse.quote(next_page) #统一编码成utf-8
                url += next_page
                
                mf = request.urlopen(url)
                c = mf.readall()
                c = str(c,encoding = 'utf-8')
 
                song = extractSongRawData(c)
                songList += extractSongInfo(song) #find all results

        for i in range(len(songList)): #print the result
            index = ''
            if i<9:
                index = '0' + str(i+1)
            else:
                index = str(i + 1)
                
            print(index + '  ' + str(songList[i]))
            
            

if __name__ == '__main__':
    main()
