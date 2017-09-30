
def SquarerootNR(x,eplison):
    assert x>=0, 'x must be non negtive not'+str(x)
    assert eplison>0,'eplison must be positive not'+str(eplison)
    x=float(x)
    guess=x
    diff=guess**2-x
    ctr=1
    while abs(diff)>eplison and ctr<=100:
        guess=guess-diff/(2*guess)
        diff=guess**2-x
        ctr+=1
    assert ctr<=100 ,'the times of iteration is too much'
    print 'NR method:'
    print 'guess: %f iteration: %d' %(guess,ctr)
    return guess