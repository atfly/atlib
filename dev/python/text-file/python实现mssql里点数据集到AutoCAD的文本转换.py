
#!/usr/bin/env python
# -*- coding: cp936 -*-
'''
功能说明：
实现从supermap后台的mssql里点数据集到AutoCAD里文本型的转换。
要是改为多线程的效果可能会更好。但现在的处理量很小，用不着给自己找麻烦
2011-10-4~2011-10-5
TODO:程度里的try...except太多，有些可以改成with语句。
'''
__author__ = 'shifeng'

import pyodbc
import logging
import comtypes.client
import numbers
import array
import re
import ConfigParser

def getconnect(db_type=None,db_arg=None):
    '''
    sql server:
        connector=pyodbc.connect('DRIVER={SQL SERVER};SERVER=LUOBO\\SQLEXPRESS;DATABASE=chengguuo')
    '''
    if db_type in ('MSSQL','JET'):
        try:
            connector = pyodbc.connect(db_arg)
        except :
            logging.error("数据库连接错误！")
            raise
        return connector

def getdrawscript(f=None):
    '''
    如果给定文件名则打开该CAD文件。
    如果没有给定文件名则认为待编辑的CAD文件已经打开。
    '''
    if not f:
        try:
            cad=comtypes.client.GetActiveObject('AutoCAD.Application') #这个可能有点问题
            cad.Visible=False
            drawingscript=cad.ActiveDocument
        except :
            logging.error("获得活动cad文件失败。请查看草稿文件是否已经打开，或请关闭除了草稿文件以外的所有cad文件。")
            raise
    else:
        try:
            cad=comtypes.client.CreateObject('AutoCAD.Application')
        except :
            logging.error("请确定本机上安装了autocad")
            raise
        try:
            drawingscript=cad.Documents.Open(f)
        except :
            logging.error("cad文件打开失败。")
            cad.Quit()
            raise
    return drawingscript

def getrows(sqlstring,connect=None,*args,**kargs):
    '''
    当返回大量记录时可以要占用大量内存空间
    >>> sqlstring = 'SELECT SmX,SmY,name FROM SMDTV_93'
    >>> connect = pyodbc.connect('DRIVER={SQL SERVER};SERVER=LUOBO\\SQLEXPRESS;DATABASE=chengguuo')
    >>> rows = getrows(sqlstring,connect)
    >>> isinstance(rows,list)
    True
    >>> row=rows[1]
    >>> isinstance(row[0],numbers.Real)
    True
    >>> isinstance(row[1],numbers.Real)
    True
    >>> isinstance(row[2],str)
    True
    '''
    cursor=connect.cursor()
    try:
        cursor.execute(sqlstring)
        rows = cursor.fetchall()
    except :
        logging.error("数据库进行sql查寻时出错")
        raise
    finally:
        connect.close()
    return rows # 返回引用，注意防止修改

def drawtext(x=None,y=None,text='什么都没有',draw=None,size=50):
    '''
    在cad里输入文字。
    >>> drawtext(x=36395514.9324,y=3250445.33498,text=r'\A1;T{\H0.7x;\S^3;}x',draw=getdrawscript('D:\\Drawing11.dwg')) == 0
    True
    '''
    if isinstance(x,numbers.Real) and isinstance(y,numbers.Real) and text: #无文字则不绘
        point=array.array('d',[x,y,0])
        try:
            ms=draw.ModelSpace #draw必须没有关闭
            #draw.ModelSpace.AddText(text,point,size) #单行文本
            ms.AddMText(point,size,text) #多行文本
        except:
            logging.error("绘制文字出错！")
            logging.error("\nx:%s\ny:%s\ntext:%s\npoint:%s\ndraw:%s\nms:\s"%(x,y,text,point,draw,ms))
            draw.Application.Quit()
            raise
        return 0
    return 1

def removesharp(text):
    '''
    去掉text中的表示supermap标签专题图上下标的特殊符号
    >>> removesharp("T#-3#=x")
    'T3x'
    >>> removesharp("J#-2#=S#+2")
    'J2S2'
    >>> removesharp("")
    ''
    >>> removesharp(None)
    ''
    '''
    if text:
        sharppattern=re.compile(r'#[+-=]')
        modifiedtext=sharppattern.sub(r"",text,count=0)
    else:
        modifiedtext=""
    return modifiedtext

def addchinesenote(test):
    pass


def sharp2mtext(text):
    '''
    >>> text1 = 'T#-3#=x'
    >>> text2 = 'J#-2#=S#+2'
    >>> text3 = None
    >>> sharp2mtext(text1) == '\\A1;T{\H0.7x;\\\\S^3;}x'
    True
    >>> #注意这是用的是repr()函数输出。
    >>> print sharp2mtext(text1)
    \A1;T{\H0.7x;\\S^3;}x
    >>> sharp2m
2000

text(text2) == '\\A1;J{\H0.7x;\\S^2;}S{\H0.7x;\\S2^;}'
    True
    >>> sharp2mtext(text3) == ''
    True
    '''
    if not text:
        return ''
    else:
        ws=text.split('#')
        logging.info(ws)
        ws_conved=[]
        for w in ws[1:]:
            w_tem=''
            if w[0] == '+':
                w_tem = r'{\H0.7x;\S' + w[1:] + r'^;}'
            elif w[0] == '-':
                w_tem = r'{\H0.7x;\S^' + w[1:] + r';}'
            elif w[0] == '=':
                w_tem = w[1:]
            ws_conved.append(w_tem)
        text_conved = r'\A1;'+ws[0]+''.join(ws_conved)
        return text_conved

def main(*args,**kargs):
    '''
    >>> #main(filename="D:\\Drawing1.dwg",sqlstring="SELECT SmX,SmY,name FROM SMDTV_93")
    0
    >>> # main(filename="D:\\Drawing2.dwg",sqlstring="SELECT SmX,SmY,name FROM SMDTV_93") 失败，由于Drawing2.dwg还不存在
    >>> # 0
    >>> config = ConfigParser.ConfigParser()
    >>> config.read('dot2text.cfg')
    ['dot2text.cfg']
    >>> connectstring = config.get('APPLICATION','connectstring')
    >>> connectstring='DRIVER={SQL SERVER};SERVER=LUOBO\\SQLEXPRESS;DATABASE=chengguuo'
    >>> filename = config.get('APPLICATION','outputfile')
    >>> sqlstring = config.get('APPLICATION','sqlstring')
    >>> dbtype =config.get('APPLICATION','dbtype')
    >>> main(filename=filename,sqlstring=sqlstring,dbtype=dbtype,connectstring=connectstring)
    0
    '''
    try:
        filename=kargs['filename']
        sqlstring=kargs['sqlstring']
        dbtype=kargs['dbtype']
        connectstring=kargs['connectstring']
    except:
        logging.info("请给出正确的关键字参数")
        return 1
    if not filename:
        draw=getdrawscript()
    else:
        draw=getdrawscript(filename)

    try:
        layer=draw.Layers.Add("DOT_2_TEXT") #新增图层
        draw.ActiveLayer=layer
    except :
        logging.error("添加新图层出错")
        draw.Application.Quit()
        raise
    # 这里出过大bug，主要是异常的处理
    #try:
    #    dbconnect=getconnect(db_type=dbtype,db_arg=connectstring)
    #except:
    #    raise
    #finally:
    #    draw.Application.Quit()
    try:
        dbconnect=getconnect(db_type=dbtype,db_arg=connectstring)
    except:
        draw.Application.Quit()
        raise
    try:
        rows=getrows(sqlstring,dbconnect)
    except:
        return 1
    try:
        for row in rows:
            #drawtext(x=row[0],y=row[1],text=removesharp(row[2]),draw=draw)
            drawtext(x=row[0],y=row[1],text=sharp2mtext(row[2]),draw=draw)
        draw.save()
    except:
        logging.error("主函数中的drawtext操作出错")
        logging.error("drawtext:\nrow[0]:%s\nrow[1]:%s\nrow[2]:%s\n"%(row[0],row[1],row[2]))
        return 1
    draw.Application.Quit()
    return 0

if __name__ == "__main__":
    #filename = raw_input("请输入文件名\n") # D:\Drawing1.dwg
    #sqlstring = raw_input("***请不要误操作！***\n请输入查询语句。\n") # select SmX,SmY,name from SMDTV93
    config = ConfigParser.ConfigParser()
    config.read('dot2text.cfg')
    connectstring = config.get('APPLICATION','connectstring')
    filename = config.get('APPLICATION','outputfile')
    sqlstring = config.get('APPLICATION','sqlstring')
    dbtype =config.get('APPLICATION','dbtype')
    main(filename=filename,sqlstring=sqlstring,dbtype=dbtype,connectstring=connectstring)


[APPLICATION]
connectstring =DRIVER={SQL SERVER};SERVER=LUOBO\SQLEXPRESS;DATABASE=chengguo
outputfile =D:\Drawing1.dwg
dbtype =MSSQL
sqlstring =SELECT SmX,SmY,name from SMDTV_93
