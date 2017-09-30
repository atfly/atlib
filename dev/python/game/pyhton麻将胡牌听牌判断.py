
#-*- coding: utf-8 -*-

import random

'''
' 麻将牌数据结构　万　1x |　筒　2x | 条　3x|　东西南北中发白　41-47
'''
class game():

    TYPE = 10 # 只有万字牌（筒和条不放进来）

    def __init__(self):
        self.leave = []
        self.user = []
	self.check = Check()
        #self.leave_bak = []
        self.create()

    # 创建牌数据
    def create(self):
        for i in range(4):
            start = game.TYPE
            for j in range(start,start+9):
                self.leave.append(j)
            for k in range(41,48):
                self.leave.append(k)
    

class Check():
    def __init__(self):
	pass

    def bar(self,_list):
	rs = self.findSame(_list,4)
	return rs
    
    def bump(self,_list):
	rs = self.findSame(_list,3)
	return rs
    
    def findSame(self,_list,num):
	return _list.count(_list[0]) == num

    def eat(self,_list):
	return _list[1] == _list[0] + 1 and _list[1] == _list[2] - 1
	    
    def hasBar(self,_list):
	pass

    def win(self,_list, j):
	if len(_list) == 0 : return True
	for i in _list:
	    #print _list
	    if _list[0] < 40: #只有字牌可以吃
	    	if len(_list) >= 3 and self.eat(_list) : #常规吃判断
		    return self.win(_list[3:],j)
	    
	    	if len(_list) >= 6 : #11 22 33 三小对吃类型
	    	    _l = [_list,_list[2:],_list[4:]]
	    	    rs = False
	    	    for k in _l : rs = self.findSame(k,2)
	    	    if rs and self.eat([_list[0],_list[2],_list[4]]):
		        return self.win(_list[6:],j)

	    if self.bump(_list) : #碰
		return self.win(_list[3:],j)
	    
	    if _list.count(_list[0]) == 2 and j == False : #　将
		j = True
		return self.win(_list[2:],j)
		    
	    break #不断的话会重复判断
	return False


class User():
    def __init__(self,_uid):
        self.uid = _uid
        self.bird = []


def main():
    _game = game()
    num = 200
    for i in range(num):
	random.shuffle(_game.leave)
	_l = _game.leave[:14]
	_l.sort()
	rs = _game.check.win(_l,False)
	print i,_l,rs
	_game.create()
            
if __name__ == '__main__':
    main()


第二版：
新增听牌判断
如果落听Check.lis会有数据

#-*- coding: utf-8 -*-

import random

'''
' 麻将牌数据结构　万　1x |　筒　2x | 条　3x|　东西南北中发白　41-47
'''
class game():

    TYPE = 10 # 只有万字牌（筒和条不放进来）

    def __init__(self):
        self.leave = []
        self.user = []
        self.check = Check()
        #self.leave_bak = []
        self.create()
	

    # 创建牌数据
    def create(self):
        for i in range(4):
            start = game.TYPE
            for j in range(start,start+9):
                self.leave.append(j)
            for k in range(41,48):
                self.leave.append(k)
    
    # 
    def getBird(self):
        random.shuffle(self.leave)
        print 'last%s'%self.leave
        self.user.append(User('roy'))
        self.user.append(User('tt'))

        for i in self.user:
            i.bird = self.leave[:13]
            i.bird.sort()
            self.leave = self.leave[13:]
            print 'user %s bird %s'%(i.uid,i.bird)
	
        print 'next%s'%self.leave
class Check():

    def __init__(self):
        self.gn = 0 # 排列组合数目　胡牌是五组
        self.lis = []

    def bar(self,_list):
	    rs = self.findSame(_list,4)
	    return rs
    
    def bump(self,_list):
	    rs = self.findSame(_list,3)

	    return rs
    
    def findSame(self,_list,num):
	    return _list.count(_list[0]) == num

    def eat(self,_list):
        _eat = None
        _rs = None
        iseat = False
        if _list[1] == _list[0] + 1 and _list[1] == _list[2] - 1 : 
            _eat = _list[:3]
            _rs = _list[3:]
            iseat = True
        if _list[2] == _list[1] + 1 and _list[2] == _list[3] and _list[2]==_list[4]-1: 
            _eat = [_list[0]]+[_list[2]]+[_list[4]]
            _rs = _eat+_list[6:]
            iseat = True
        return (_eat,_rs,iseat)
	    
    def hasBar(self,_list):
	    pass
    def checklis(self,_list):
        if len(self.lis) > 0 : return False
        if len(_list) > 3 : return False
        if len(_list) < 3 : return True
        def isLis(_l):
            if _l[0] == _l[1] : return True
            if _l[0] == _l[1] - 1 : return True
            if _l[0] == _l[1] - 2 and (_l[0] + 1)%10 != 0 : return True
        if isLis(_list) : return True
        if isLis(_list[1:]) : return True
        return False

    def win(self,_list, j):
        if len(_list) == 0 : return True
        for i in _list:
            #print _list,j
            if i < 40: #只有
48d3
字牌可以吃
                (_eat,_rs,iseat) = self.eat(_list)
                if iseat : #常规吃判断
                    self.gn += 1
                    print 'get eat',_eat,_rs,j
                    if self.win(_rs,j) : return True
                    if self.checklis(_rs):
                        self.lis = _rs
                        return False
                    else:
                        break
	    
            if self.findSame(_list,3): #碰
                self.gn += 1
                print 'get bump',_list[:3],j
                arr = _list[3:]
                if self.win(arr,j) : return True
                if self.checklis(arr):
                    self.lis = arr
                    return False
                else:
                    break
	        
            if self.findSame(_list,2) and j == False : #将
                j = True
                self.gn += 1
                print 'get j ',_list[:2],j
                arr = _list[2:]
                if self.win(arr,j) : return True
                if self.checklis(arr) : 
                    print 'get j check',arr
                    self.lis = arr
                    return False
                    
        return False


class User():
    def __init__(self,_uid):
        self.uid = _uid
        self.bird = []


def main():
    _game = game()

    _l = [11,11,12,12,13,13,16,16,16,17,17,18,41,41]
    _game.check.gn = 0
    rs = _game.check.win(_l,False)
    gn = _game.check.gn
    #lis = _game.check.lis
    #_game.check.gn = 0
    print _l,rs,gn,_game.check.lis

    '''
    num = 2000
    for i in range(num):
	random.shuffle(_game.leave)
	_l = _game.leave[:14]
	_l.sort()
	rs = _game.check.win(_l,False)
	if rs : print i,_l,rs
	_game.create()
    '''
            
if __name__ == '__main__':
    main()
