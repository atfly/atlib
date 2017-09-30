
#!/usr/bin/python

import os
import pickle


if os.path.exists(r'E:\Person.data')==False:
    f=open('E:\Person.data','wb')
    temp={'total' : 0}
    pickle.dump(temp,f)
    f.close()
else:
    pass


def add():
    f=open('E:\Person.data','rb')
    a=pickle.load(f)
    f.close()
    b=0
    name = input('请输入所要添加联系人的姓名:')
    for key in a.keys():
        b+=1
        if key==name and b <= a['total']+1:
            print("联系人已存在，添加失败！")
            break
        if b==a['total']+1 and key != name:        
            number = input('请输入号码:')
            information={name : number}
            a['total']+=1
            a.update(information)
            f=open('E:\Person.data','wb')
            pickle.dump(a,f)
            f.close()
            print('添加成功!')
            break

def showall():
    f=open('E:\Person.data','rb')
    a=pickle.load(f)
    print("一共有{}个联系人.".format(a['total']))
    for key in a.keys():
        if key != 'total':
            print("{""}:{""}".format(key,a[key]))
    f.close()

def exit():
    exec("quit()")
#查找
def search(name):
    f=open('E:\Person.data','rb')
    a=pickle.load(f)
    b=0
    for key in a.keys():
        b+=1
        if key==name and b<=a['total']+1:
            print("{}的号码是: {}".format(name,a[key]))
            break
        if b==a['total']+1 and key != name:
            print("联系人不存在!")
            break
    f.close()
#删除
def deleate(name):
    f=open('E:\Person.data','rb')
    a=pickle.load(f)
    f.close()
    b=0
    for key in a.keys():
        b+=1
        if key==name and b<=a['total']+1:
            a.pop(name)
            a['total']-=1
            f=open('E:\Person.data','wb')
            pickle.dump(a,f)
            f.close()
            print("删除成功!")
            break
        if b==a['total']+1 and key != name:
            print("联系人不存在！无法删除！")
            break
#修改
def change ():
    x=input("请输入所要修改联系人姓名:")
    f=open('E:\Person.data','rb')
    a=pickle.load(f)
    f.close()
    b=0
    for key in a.keys():
        b+=1
        if key==x and b<=a['total']+1:
            y=input("请输入修后的号码:")
            a[key]=y
            f=open('E:\Person.data','wb')
            pickle.dump(a,f)
            f.close()
            print("修改成功!")
            break
        if b==a['total']+1 and key != name:
            print("联系人不存在！")
            break

#界面www.iplaypy.com
def point ():
    print("*******************************")
    print("显示提示信息:*")
    print("显示所有联系人:0")
    print("查找联系人:1")
    print("添加联系人:2")
    print("删除联系人:3")
    print("更改联系人资料:4")
    print("退出通讯录:5")
    print("*******************************")
#主程序
point()
while True:
    x=input("请输入您的选择:")
    if x == '2':
        add()
        continue
    if x== '0':
        showall()
        continue
    if x=='5':
        exit()
        continue
    if x=='1':
        name=input("请输入所要查找联系人的姓名:")
        search(name)
        continue
    if x=='3':
        name=input("请输入所要删除联系人的姓名:")
        deleate(name)
        continue
    if x== '4':
        change()
        continue
    if x=='*':
        point()
    else:
        print("输入选项不存在，请重新输入！")
        continue