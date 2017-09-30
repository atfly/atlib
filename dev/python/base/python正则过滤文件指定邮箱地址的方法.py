
#coding=utf8
# 过滤掉域名为10个字符的邮箱

import re
import os
import sys

def mail_filter(srcfile, pattern):
    fin = open(srcfile, 'r')

    for line in fin:
        pat = re.compile(pattern)
        m = pat.match(line)

        # 没有匹配则输出
        if not m:
            print line, 

    fin.close()

#www.iplaypy.com

if __name__ == '__main__':
    srcfile = 'in'
    destfile = 'out'

    # 重定向标准输出到文件
    fout = open(destfile, 'w')
    sys.stdout = fout

    mail_filter(srcfile, r'\w{10}@\w*\.\w*')

    fout.close()

