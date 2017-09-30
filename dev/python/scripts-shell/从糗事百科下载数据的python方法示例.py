
#encoding:utf-8

import sqlite3,urllib2,re,glob

_database='db.sqlite3'
_cn=sqlite3.connect(_database)
c=_cn.cursor()

findById='select * from qiu where id=?'
findByStatus='select * from qiu where status=?'
findContentNotEmpty='select * from qiu where content<>""'
deleteById='delete * from qiu where id=?'
insertId='insert into qiu(id) values(?)'
insert='insert into qiu(id,content,status) values(?,?,?)'
updateContentAndStatusById='update qiu set content=?,status=? where id=?'


def getRowCount(c):
  row=c.fetchall()
  return(len(row))

class qparser():
  
  def __init__(self,id):
    self.page_id=id
    self.url=self.getUrl(self.page_id)
    self.getPage()
    p=self.pageParser()
    if p[0]:
      self.updateDB(p)
  
  def getUrl(self,i):
    return("http://www.qiushibaike.com/articles/"+str(i)+".htm")
  
  def getPage(self):
    try:
      print('downloading '+self.url+'...')
      content=urllib2.urlopen(self.url).read()
      #print content
      print('download '+self.url+' finished')
      self.content=content
    except:
      self.content=''
      print('download '+self.url+' error')

#www.iplaypy.com  

  def getContent(self,page):
    try:
      begin=page.find(r'<div class="content"')+25
      page=page[begin:]
      end=page.find(r'<div')-4
      page=page[:end]
      page.replace(r'<br />','').replace('\n','')
      return(page)
    except:
      return('')
  
  def pageParser(self):
    page=self.content
    print('parsing the page')
    result=[None]*3
    recontent=r'<div class=\"content\">\s+(.*)\s+'
    relast=r'<a href=\"\/articles\/(.*)\.htm\">&lt;<span class=\'ad\'> <\/span>上一糗事<\/a>'
    renext=r'<a href=\"\/articles\/(.*)\.htm\">下一糗事<span class=\'ad\'>'
    
    p=page
    result[0]=self.getContent(p)
    
    matches=re.findall(relast,page)
    if len(matches)>0:
        result[1]=matches[0]
        
    matches=re.findall(renext,page)
    if len(matches)>0:
        result[2]=matches[0]
        
    print('parsed the page')
    
    return(result)
    
  def updateDB(self,p): 
    content=p[0]
    last=p[1]
    next=p[2]
    
    if last:
      c.execute(findById,(last,))
      l=getRowCount(c)
      if l==1:
        c.close()
      elif l>1:
        c.close()
        c.execute(deleteById,(last,))
        c.execute(insertId,(last,))
        _cn.commit
      else:
        c.close()
        c.execute(insertId,(last,))
        _cn.commit
    
    if next:
      c.execute(findById,(next,))
      l=getRowCount(c)
      if l==1:
        c.close()
      elif l>1:
        c.close()
        c.execute(deleteById,(next,))
        c.execute(insertId,(next,))
        _cn.commit()
      else:
        c.close()
        c.execute(insertId,(next,))
        _cn.commit()
        
    if last and next:
      c.execute(findById,(self.page_id,))
      l=getRowCount(c)
      if l>1:
        c.close()
        c.execute(deleteById,(self.page_idid,))
        c.execute(insert,(self.page_id,content,1))
        _cn.commit()
      else:
        c.close()
        c.execute(updateContentAndStatusById,(content,1,self.page_id))
        _cn.commit()
    else:
      c.execute(updateContentAndStatusById,(content,1,self.page_id))
      _cn.commit()

class downloader():

  def __init__(self):
    idList=self.getIdList()
    while len(idList)!=0:
      for i in idList:
        q=qparser(i)
      self.DbToText()
      idList=self.getIdList()
      
  def getIdList(self):
    idList=[]
    c.execute(findByStatus,(0,))  
    for i in c:
      idList.append(i[0])
    c.close()
    return(idList)
  
  def DbToText(self):
    c.execute(findContentNotEmpty)
    txtList=glob.glob('*.txt')
    txtList=[i[0:-4] for i in txtList]
    for i in c:
      id=i[0]
      content=i[1].replace(r'<br />','').replace('\n','')
      if id not in txtList:
        fileName=self.makeFileName(id)
        open(fileName,'w').write(content.encode('gbk'))
  
  def makeFileName(self,i):
    return(str(i)+'.txt')

def main():
  d=downloader()

if __name__=='__main__':
  main()
