//match函数只检测RE是不是在string的开始位置匹配， search会扫描整个string查找匹配
def isMatch(pattern,text):
    if re.compile(pattern).search(text):
        return 1
    else:
        return 0