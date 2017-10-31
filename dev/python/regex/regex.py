#match函数只检测RE是不是在string的开始位置匹配， search会扫描整个string查找匹配
def isMatch(pattern,text):
    if re.compile(pattern).search(text):
        return 1
    else:
        return 0
        

========================================================================================================
#通过类来封装所有的正则的表达式		
import re

class Reg_Exp(object):
    # 定义如下模式(剔除html残余的一些字符)
    pt1 = re.compile("nbsp|0pt'>")
    # 年月
    pt2 = re.compile('\d{2,4}年\d{1,2}月')
    # 先匹配非全日制的
    r0 = re.compile(u'自考|远程|成教|网络教育|继续教育|网络学院|自学考试|成人教育|函授|远程教育|电视大学|电大^(学)')
    # 高中
    r1 = re.compile(u'职高|中学|([一二三四五六七八九十]+|[0-9])中|高中')
    # 中专技校
    r2 = re.compile(u'职业学校|职校|技校|技工学校|培训学校|[^(高等专科|税务专科|师范专科|医学专科)]学校')
    # 国外大学
    r3 = re.compile('academy|institute|school|college|association|univ.*')
    # 全部中文的大学
    r4 = re.compile(r'大学|学院|专科学校|研究所|研究院|中科院')
    pattern1 = re.compile('academy|institute|school|college|association|univ.*')
    pattern2 = re.compile('academy|institute|school|college|association|univ.*|of|the|and|for')
    pattern3 = re.compile('[^\u4e00-\u9fa5a-zA-Z ]')
    pattern4 = re.compile('[^a-zA-Z ]')