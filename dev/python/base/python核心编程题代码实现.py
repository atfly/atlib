
#coding:utf-8
"""
设计一个"石头,剪子,布"游戏,有时又叫"Rochambeau",你小时候可能玩过,下面是规则.你和你的对手,在同一时间做出特定的手势,必须是下面一种手势:石头,剪子,布.胜利者从
下面的规则中产生,这个规则本身是个悖论. 
(a) 布包石头. 
(b)石头砸剪子, 
(c)剪子剪破布.在你的计算机版本中,用户输入她/他的选项,计算机找一个随机选项,然后由你
的程序来决定一个胜利者或者平手.注意:最好的算法是尽量少的使用 if 语句.

黄老师写于2013-4-8下午，在终端下运行python *.py
不同的平台可能会出现汉字编码问题。
在mac os 终端测试过。

guess_list = ["石头","剪刀","布"]
guize = [["布","石头"],["石头","剪刀"],["剪刀","布"]]



computer = random.choice(guess_list)
people =  raw_input('请输入：石头,剪刀,布\n').strip()
 
if   computer ==  people:
     print "平手，再玩一次！"
    
elif [computer,people] in guize :
     print "电脑获胜！"
else:
    
    print "人获胜！"
改写为英文版。
"""
import random

guess_list = ["stone","Scissors","Cloth"]
guize = [["Cloth","stone"],["stone","Scissors"],["Scissors","Cloth"]]



computer = random.choice(guess_list)
people =  raw_input('please input：stone,Scissors,cloth\n').strip()
 
if   computer ==  people:
     print "No-win！"
    
elif [computer,people] in guize :
     print "computer Victory！"
else:
    
    print "People Victory！"