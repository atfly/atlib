
#python list 排序

def my_key1(x):
    return x % 10
aList = [4, 5, 1, 2, 12, 34, 56, 9 ,80]
aList.sort() #默认按升序排列
print(aList)

aList.sort(reverse = True) #按降序排列
print(aList)

#www.iplaypy.com

aList.sort(key = my_key1) #根据key函数，按照个位数进行升序排列
print(aList)

def my_key2(x):
    return x[1]
aList = [(4,'ab'), (56,'c'), (1,'bb'), (102, 'a')]
aList.sort(key = my_key2) #按照每个元组的第2分量，即字符串排序
print(aList)

