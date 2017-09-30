
#len( CG(7, 3) ) == 7*6*5/3*2*1
def CG(n, m):

    assert m >= 1

    if m == 1:
        for i in range(n):
            yield [i]
    else:
        for v in CG(n, m-1):
            for i in range(v[-1]+1, n):
                yield v + [i]


def CG2(n, m):
     
     if m == 1: # assert m >= 1
         return [[i] for i in range(n)]

     else:
         return [v + [i] for v in CG(n, m-1) for i in range(v[-1]+1, n)]
 

#-----www.iplaypy.com-----组合C(n, m)的大小, Combination Count


def CC(n, m):
  mul=1
  div=1

  for i in range(1, m+1):
    mul *= (n-i+1)
    div *= i

  return mul/div

