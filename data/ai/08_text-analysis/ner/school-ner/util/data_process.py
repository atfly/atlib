#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/26 17:21
# @Author  : skydm
# @Site    : 
# @File    : data_process.py

import pymysql
import configparser
import html
from autocorrect import spell
from code_construct.Main_Scripts.util.reg_exp import Reg_Exp

# filePath = os.path.dirname(__file__) + '/../API/data/config.ini'
filePath ='C:/Users/wangwei/PycharmProjects/work/code_construct/Main_Scripts/data/config.ini'
# 读取配置文件
config = configparser.ConfigParser()
config.read(filePath)
ip = config.get("global", "host")
port = int(config.get("global", "port"))
user = config.get("global", "user")
passwd = config.get("global", "passwd")
db = config.get("global", "db")
charset = config.get("global", "charset")

r = Reg_Exp()

# 获取数据表中的数据
def get_data(table, *fields):
    school_list = []
    # conn = pymysql.connect(host=ip, port=port, user=user, passwd=passwd, db=db, charset=charset)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='8610912', db='resume', charset='utf8')
    cur = conn.cursor()
    field_str = ""
    for field in fields:
        field_str = field_str + field + ","
    field_str = field_str[:-1]
    sql = "SELECT %s FROM %s" % (field_str, table)
    # print(sql)
    cur.execute(sql)
    results = cur.fetchall()
    for r in results:
        school_list.append(r)
    conn.close()
    return school_list

# 预处理以及过滤掉简写错误的字典库的数据
def preprocess(school):
    # 剔除html转义字符
    school = html.unescape(school)
    # 剔除自定义模式中的字符
    school = r.pt1.sub('', school)
    # 删除年月
    school = r.pt2.sub('', school)
    # 再进一步剔除特殊字符
    school = r.pattern3.sub( '', school).strip()
    # 大小写转换
    school = school.lower()
    return school

# 判断学是否是特殊类型(全日制还是非全日制(函授,成教,自考))
def judge_special(school):
    if r.r0.search(school) != None:
        return False
    else:
        return True

def judge_type(school):
    if r.r1.search(school) != None:
        return 1  # 高中
    elif r.r2.search(school) != None:
        return 2  # 中专技校
    elif r.r3.search(school) != None:
        return 3  # 国外大学
    else:
        return 4  # 可能是高校或者非学校

def is_school(school):
    if school == 'Unknown' or school == '':
        return 0
    else:
        return 1

def get_spell(school_set):
    # 拼写错误检查
    new_school_set = set([spell(i) for i in school_set if i != ''])
    return new_school_set