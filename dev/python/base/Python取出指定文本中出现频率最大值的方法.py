
from time import time
from operator import itemgetter

def test():
    # 取 10 个，有需要可以修改, 及定义读取的文件 test.txt 
    iList = 10
    strFileName = 'test.txt'

    count = {}
    for word in open(strFileName).read().split():
        if count.has_key(word):
            count[word] = count[word] + 1
        else:
            count[word] = 1
    print sorted(count.iteritems( ), key=itemgetter(1), reverse=True)[0:iList]

# 调用www.iplaypy.com
if __name__ == '__main__':
    t1 = time()
    test()
    print time()-t1

