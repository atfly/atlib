
def f1(a,b,n):
    intDigits=lambda n: map(int, str(n))
    return reduce(lambda x,y: x+intDigits(sum(x[-2:])), range(n-2), [a,b])[n-1]

test=[[1,1,2],[1,1,8],[1,4,8]]
print [f1(*i) for i in test]
partition=lambda L: [L[i:i+2] for i in range(len(L)-1)]
intDigits=lambda n: map(int, str(n))

def f2(a,b,n):
    r=[a,b]
    while r[-2:] not in partition(r[:-2]):
        r=r+intDigits(r[-2]+r[-1])
    pos= partition(r).index(r[-2:])
    return r[n-1 if n<pos else (n-1-pos)%(len(r)-pos-2) + pos]

test=[[1,1,2],[1,1,8],[1,4,8],[2,4,100],[1,5,10**8-1],[1,7,10**8]]
print [f2(*i) for i in test]