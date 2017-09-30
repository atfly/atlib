
people={
    'Alice':{
        'phone':'2341',
        'addr':'Foo drive'
        },
     'Beth':{
        'phone':'9102',
        'addr':'bar street 42'
         },
      'Cecil':{
         'phone':'3158',
         'addr':'Baz avenue 90'
          }
    }
labels={
        'phone':'phone number',
        'addr':'address'
    }

#初始化名字
names=input('Name:')
name=name.strip()

#获取选项
r=input('Please choose  phone(q) or addr(a):')

#初始化q和a
q='q' 
a='a'
s=str(r)

#www.iplaypy.com
#获取键
if  q==s.strip(): y='phone' 
if  a==s.strip(): y='addr'
d="%s's %s is %s."
value=(name,labels[y],people[name][y])

#查找
if name in people: print(d %value)