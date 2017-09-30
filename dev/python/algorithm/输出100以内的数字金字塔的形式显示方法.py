
a = 1
b = 2
print
for i in range(1, 101):
    print i,
    if i == a:
        print
        a = a+b
        b = b+1