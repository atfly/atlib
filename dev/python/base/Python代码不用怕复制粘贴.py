
# fib.py
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    #:
    print()
#:
fib(1000)

def end():
    pass

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    end
    print()
end
fib(1000)

end = None

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    end
    print()
end
fib(1000)
