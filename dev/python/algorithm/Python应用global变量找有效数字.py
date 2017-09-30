

g_count = 0

def APfirst(num):
    global g_count
    g_count = 0
    return int(str(num)[0])

def APnext(num):
    global g_count
    if(g_count < len(str(num))-1):
        g_count = g_count + 1
    return int(str(num)[g_count])

#www.iplaypy.com

input_num = 1234567890
print(APfirst(input_num))

for i in range(0,11):
    print(APnext(input_num))

print(APfirst(input_num))
print(APnext(input_num))
