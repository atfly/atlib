# !/usr/bin/python
# -*- coding:utf-8 -*-
import csv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    path = 'Advertising.csv'
    print '''############手写读取数据############'''
    f = file(path)
    x = []
    y = []
    # i 是行的index，d 是str类型
    for i, d in enumerate(f):
        # 忽略到首行title
        if i == 0:
            continue
            # 方法用于移除字符串头尾指定的字符（默认为空格）
        d = d.strip()
        # 如果d是空
        if not d:
            continue

        d = map(float, d.split(','))
        x.append(d[1:-1])
        y.append(d[-1])
    print(x)
    print(y)
    x = np.array(x)
    y = np.array(y)
    print '''############手写读取数据2############'''
    with open(path, 'r') as f:
        data = f.read()
        print data

    print '''############Python自带库############'''
    f = file(path, 'r')
    print f
    d = csv.reader(f)
    for line in d:
        print line
    f.close()

    print '''############Numpy读入############'''
    p = np.loadtxt(path, delimiter=',', skiprows=1)
    print p

    print '''############Pandas读入############'''
    data = pd.read_csv(path)  # TV、Radio、Newspaper、Sales
    x = data[['TV', 'Radio', 'Newspaper']]
    # x = data[['TV', 'Radio']]
    y = data['Sales']
    print x
    print y
