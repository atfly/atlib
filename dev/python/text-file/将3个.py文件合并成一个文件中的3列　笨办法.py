
"""
python 3个文件合并成3列.py
依山居 7:47 2015/12/15
先写个简单的实现。主要是itertools.zip_longest()的用法
"""

import itertools

with open("1.txt") as f:
    txt1=[r.rstrip("\n") for r in f.readlines()]
with open("2.txt") as f:
    txt2=[r.rstrip("\n") for r in f.readlines()]
with open("3.txt") as f:
    txt3=[r.rstrip("\n") for r in f.readlines()]

result=itertools.zip_longest(txt1,txt2,txt3,fillvalue=' ')
#[print(r) for r in result]

with open("result.txt","w+") as f:
    [f.write(','.join(r)+"\n") for r in result]
