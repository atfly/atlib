
class Tobj(object):

    def __init__(self, serial, val=0):
        self.serial = serial
        self.val = val
    
    def __repr__(self):
        return "%s(%s)" % (
            self.__class__.__name__,
            ', '.join([
                "%r:%r" % (k, v)
                for k, v in self.__dict__.items()
                ])
            )

def init(L):
    return [
        Tobj(i)
        for i in range(L)
        ]


def show():
    for obj in objlst:
        print obj


def serialset(val=1):
    for obj in objlst:
        obj.val = val

def randomset(val=2):
    for i in xrange(len(objlst)):
        objlst[i].val = val

def tester():
    serialset(1)
    show()
    randomset(2)
    show()


if __name__ == "__main__":
    objlst = init(1000)
    import timeit
    t1 = timeit.Timer('serialset()', "from __main__ import serialset")
    print t1.timeit()
    t2 = timeit.Timer('randomset()', "from __main__ import randomset")
    print t2.timeit()
    