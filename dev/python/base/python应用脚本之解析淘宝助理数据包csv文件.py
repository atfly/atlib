
#/usr/bin/python
# encoding=utf-8

import os

# 从当前脚本所在目录中查找csv文件
for f in os.listdir(os.path.dirname(os.path.abspath(__file__))):

    # 略过非csv文件
    if f[-4:len(f)] != '.csv':
        continue

    # 读取csv内容
    content = file(f).read()

    # 转换文件编码
    content = content.decode('utf-16').encode('utf-8')

    # 清除描述中的换行符
    content = content.replace("\r\n", '')

    # 切分行www.iplaypy.com
    for num, line in enumerate(content.split("\n")):

        # 略过空行
        if not line:
            continue

        # 切分字段
        fields = []
        for field in line.strip().split("\t"):
            fields.append(field)

        # 查看切分字段数量是否一致
        print len(fields)