
#encoding=utf-8
# -*- coding: utf-8 -*-
#将在sae上部署的博客文章html格式批量转换为github宜用的markdown样式文章
'''
把大象装冰箱分三步：
1、将test数据库中文章数据，按篇查询出来
2、将查询的文章，按markdown样式整理出来
3、整理好后另存为md文件，文件名要按日期格式走
'''
import sys 
import MySQLdb
import html2text

reload(sys) 
sys.setdefaultencoding('utf-8') 

conn=MySQLdb.connect(host="localhost",user="root",passwd="root",db="test",charset='utf8')
print conn
'''
查询文章列表
根据文章查询分类
组织写入
'''
cursor =conn.cursor()
sql ='''SELECT
      id,CONCAT(date_format(last_update,'%Y-%m-%d'),'-',slug,'.md'),title,tags,content,last_update
        FROM
            zinnia_entry where STATUS=2'''
cursor.execute(sql)
row=cursor.fetchall()
#print row
for i in row:
    print ('正在处理%s%s' % (i[2],i[3]))
    id=i[0]
    md_title=i[1]
    title=i[2].replace(': ',':')
    tags=i[3]
    content=i[4]
    last_update=i[5]
    #根据id获取分类信息
    sql2='''SELECT
            title
        FROM
            zinnia_entry_categories a,
            zinnia_category b
        WHERE
            a.category_id = b.id and entry_id=%s '''
    cursor.execute(sql2,id)
    category_row=cursor.fetchall()
    category_in=""
    q=0
    for j in category_row:
        q=q+1
        if q != len(category_row):
            category_in+=j[0]+','
        else:
            category_in+=j[0]
    print ("%s分类为：%s"%(len(category_row),category_in))
    f=open(md_title,'w')
    '''
    title: 博客优化参考
    date: 2015-06-20 23:24:13
    tags: hexo #[tag1,tag2,tag3]
    categories: 喜欢
    ---
    '''
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ul_item_mark = '-'
    h.body_width = 0
    h.hide_strikethrough = True
    f.write(('title: %s'% title)+'\n')
    f.write(('date: %s'%last_update)+'\n')
    f.write(('tags: [%s]'%tags)+'\n')
    f.write(('categories: [%s]'%category_in)+'\n')
    f.write('---'+'\n')
    f.write(h.handle(content)+'\n')
    #f.write('正文内容'+'\n')
    f.close()
    
cursor.close() 
conn.close() 