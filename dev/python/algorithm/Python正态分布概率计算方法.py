
def st_norm(u):
    '''标准正态分布'''
    import math
    x=abs(u)/math.sqrt(2)
    T=(0.0705230784,0.0422820123,0.0092705272,
       0.0001520143,0.0002765672,0.0000430638)
    E=1-pow((1+sum([a*pow(x,(i+1))
                    for i,a in enumerate(T)])),-16)
    p=0.5-0.5*E if u<0 else 0.5+0.5*E
    return(p)

def norm(a,sigma,x):
    '''一般正态分布'''
    u=(x-a)/sigma
    return(st_norm(u))

while 1:
    '''输入一个数时默认为标准正态分布
    输入三个数(空格隔开)时分别为期望、方差、x
    输入 stop 停止'''
    S=input('please input the parameters:\n')
    if S=='stop':break
    try:
        L=[float(s) for s in S.split()]
    except:
        print('Input error!')
        continue
    if len(L)==1:
        print('f(x)=%.5f'%st_norm(L[0]))
    elif len(L)==3:
        print('f(x)=%.5f'%norm(L[0],L[1],L[2]))
    else:
        print('Input error!')
#www.iplaypy.com