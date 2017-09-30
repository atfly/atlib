
def init_set8(r10=range(10)):
    """
    把循环内的range函数提到外面
    times5.486 ==> 4.427
    """
    ret = []
    for i in r10:
        for j in r10:
            for k in r10:
                for l in r10:
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        ret.append((i, j, k, l))
    return ret

timing(init_set8, 1000)

def init_set9(r10=range(10)):
    """
    for 循环改成列表推导
    times5.486 ==>3.773 
    """
    return [(i, j, k, l)
        for i in r10
        for j in r10
        for k in r10
        for l in r10
        if ( i != j and i != k and i != l and j != k and j != l and k != l) ]
timing(init_set9, 1000)

def init_set10(r10=range(10)):

    return ((i, j, k, l)
            for i in r10
            for j in r10
            for k in r10
            for l in r10
            if( i != j and i != k and i != l and j != k and j != l and k != l) )
timing(init_set10, 1000)

def init_set11():
    """
    用代码的空间代价换取计算P4_4的时间
    init_set11 1000 times 7.268 OMG
    reduce(lambda x,y:x+y,l)太慢了
    """
    c10_4=[( i, j, k, l ) for i in xrange(0, 10)
                          for j in xrange(i+1, 10)
                          for k in xrange(j+1, 10)
                          for l in xrange(k+1, 10) ]

    ret=reduce(lambda x,y:x+y,
            [ [ (i, j, k, l),
                (i, j, l, k),
                (i, k, j, l),
                (i, k, l, j),
                (i, l, j, k),
                (i, l, k, j),
                (j, i, k, l),
                (j, i, l, k),
                (j, k, i, l),
                (j, k, l, i),
                (j, l, i, k),
                (j, l, k, i),
                (k, i, j, l),
                (k, i, l, j),
                (k, j, i, l),
                (k, j, l, i),
                (k, l, i, j),
                (k, l, j, i),
                (l, i, j, k),
                (l, i, k, j),
                (l, j, i, k),
                (l, j, k, i),
                (l, k, i, j),
                (l, k, j, i),]
                for i, j, k, l in c10_4 ],
            ) 
    return ret

def init_set12():
    """
    generator是伟大的发明,数据流编程万岁
    init_set12 1000 times 1.758 
    www.iplaypy.com

    """
    c10_4=(( i, j, k, l ) for i in xrange(0, 10)
            for j in xrange(i+1, 10)
            for k in xrange(j+1, 10)
            for l in xrange(k+1, 10) )

    from  itertools import chain
    ret=chain(
        *( ( (i, j, k, l),
             (i, j, l, k),
             (i, k, j, l),
             (i, k, l, j),
             (i, l, j, k),
             (i, l, k, j),
             (j, i, k, l),
             (j, i, l, k),
             (j, k, i, l),
             (j, k, l, i),
             (j, l, i, k),
             (j, l, k, i),
             (k, i, j, l),
             (k, i, l, j),
             (k, j, i, l),
             (k, j, l, i),
             (k, l, i, j),
             (k, l, j, i),
             (l, i, j, k),
             (l, i, k, j),
             (l, j, i, k),
             (l, j, k, i),
             (l, k, i, j),
             (l, k, j, i),)
            for i, j, k, l in c10_4 )
        )  
    return list(ret)
timing(init_set12, 1000)

