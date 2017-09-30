
x = 1
def fun(a):
    b=3
    x=4
    def sub(c):
        d=b
        global x
        x = 7
        print ("Nested Function\n=================")
        print locals()

    sub(5)
    print ("\nFunction\n=================")
    print locals()
    print locals()["x"]
    print globals()["x"]

print ("\nGlobals\n=================")
print globals()

fun(2)

///scope.py

Globals
=================
{'x': 1,
 '__file__':
'C:\\books\\python\\CH1\\code\\scope.py',
 'fun': <function fun at 0x008D7570>,
 't': <class '__main__.t'>,
 'time': <module 'time' (built-in)>,. . .}

#www.iplaypy.com

Nested Function
=================
{'c': 5, 'b': 3, 'd': 3}

Function
=================
{'a': 2, 'x': 4, 'b': 3, 'sub':
    <function sub at 0x008D75F0>}
4
7