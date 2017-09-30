
#Target
class Target:
    def targetFunc(self):
        print "targetFunction"

#www.iplaypy.com
#aop
temp=Target.targetFunc

def foo(self):
    print "before call"
    temp(self)

    print "after call"

Target.targetFunc=foo

#see result
t=Target()
t.targetFunc() 