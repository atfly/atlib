
#coding=utf-8

def init_set():
    r10=range(10)
    return [(i, j, k, l)
            for i in r10 for j in r10 for k in r10 for l in r10
            if (i != j and i != k and i != l and j != k and j != l and k != l) ]

#对给定的两组数，计算xAyB.不知道能不能更快些
def get_match_ab(target, source):
    la, lb = 0, 0
    for (i, t) in enumerate(target):
        for (j, s) in enumerate(source):
            if s == t:
                if i == j:
                    la += 1
                else:
                    lb += 1
                #break this loop since we already found match
                break
    return (la, lb)

#by lancer
#思路很好，把原来的16次比较变成了8次
#经过timeit验证确实速度有所提高
def get_match_ab2(target, source):
    table = [-1] * 10
    la, lb = 0, 0
    for i in xrange(len(source)):
        table[source[i]] = i
    for i in xrange(len(target)):
        if table[target[i]] == i:
            la += 1
        elif table[target[i]] != -1:
            lb += 1
    return (la, lb)

#nums: the number_set list to be checked
#guess: last guess
#a, b: the number of aAbB
#@return: the rest number_sets which matche last guess
def check_and_remove(nums, guess, a, b):
    rest_nums = []
    for num_set in nums:
        if (a, b) == get_match_ab(num_set, guess):
            rest_nums.append(num_set)
    return rest_nums

#计算在nums中选择target以后，所有ab分支里面的剩余组合个数
def calc_ab_counts(target, nums):
    #a * 10 + b is used to indicate an "a & b" combination
    ab_map = {}
    #init ab_map
    abs = (0, 1, 2, 3, 4, 10, 11, 12, 13, 20, 21, 22, 30, 31, 40)
    for ab in abs:
        ab_map[ab] = 0
    #let's do the calculation
    for num_set in nums:
        (a, b) = get_match_ab(num_set, target)
        ab_map[a * 10 + b] += 1
    return [ab_map[ab] for ab in abs]

#计算一个选择相对于选择集的“标准差”
def calc_standard_deviation(target, nums):
    ab_counts = calc_ab_counts(target, nums)
    total = sum(ab_counts)
    avg = float(total) / len(ab_counts)
    sd = sum([(abc - avg)**2 for abc in ab_counts])
    return sd

#根据现有集合寻找下一个集合
#采用“最小标准差”作为衡量标准
def next_guess(nums):
    min_sd = 0
    min_set = ()
    touched = False
    for num_set in nums:
        sd = calc_standard_deviation(num_set, nums)
        if not touched or min_sd > sd:
            touched = True
            min_set = num_set
            min_sd = sd
    return min_set

#根据现有集合寻找下一个集合
#随机选取，会有4-5个超过八次
def next_guess2(nums):
    return nums[0]

#折衷的方法：小于500用最小标准差
def next_guess3(nums):
    if len(nums) > 500:
        return next_guess2(nums)
    else:
        return next_guess(nums)

#计算熵
import math
def calc_entropy(target, nums):
    ab_counts = calc_ab_counts(target, nums)
    total = sum(ab_counts)
    hs = []
    for abc in ab_counts:
        h = 0
        if abc:
            p = float(abc) / total
            h = p * math.log(p, 2)
        hs.append(h)
    return sum(hs)

#使用信息量作为衡量标准
def next_guess4(nums):
    min_sd = 0
    min_set = ()
    touched = False
    for num_set in nums:
        sd = calc_entropy(num_set, nums)
        if not touched or min_sd > sd:
            touched = True
            min_set = num_set
            min_sd = sd
    return min_set

def make_decision_tree():
    from Queue import Queue
    result = ((0, 1, 2, 3), {})
    queue = Queue()
    rest_nums = init_set()
    queue.put((rest_nums, result))
    #all xAyB set
    abs = [(a, b) for a in range(5) for b in range(5 - a)]

    while not queue.empty():
        (rest_nums, (guess, mapping)) = queue.get()
        for (a, b) in abs:
            new_rest_nums = check_and_remove(rest_nums, guess, a, b)
            length = len(new_rest_nums)
            if length == 1:
                if a != 4: #b can't be other than 0 when a == 4
                    mapping[a * 10 + b] = new_rest_nums[0]
            elif length > 1:
                new_guess = next_guess4(new_rest_nums) #TODO: 替换guess函数调整算法
                new_result = (new_guess, {})
                mapping[a * 10 + b] = new_result
                queue.put((new_rest_nums, new_result))
    return result

max_level = 0
level7_plus_tups = []
def pprint_result(result, level = 0):
    global max_level, max_level_tup
    (tup, mapping) = result
    print tup
    level += 1
    if level > max_level:
        max_level = level
    if len(mapping) == 0:
        print
    else:
        for key in mapping:
            val = mapping[key]
            #打印前缀
            print u"%d|\t" * level % tuple(range(1, level + 1)),
            print u"%d:" % (level + 1),
            #打印xAyB
            print u"%dA%dB" % (key / 10, key % 10),
            if len(val) == 4: #direct result
                #打印结果
                print val
                if level >= 7:
                    level7_plus_tups.append((level, val))
            else:
                pprint_result(val, level)

#来玩玩www.iplaypy.com
print u"Notice: 4A0B is NOT included, since it result to Game Over"
pprint_result(make_decision_tree())
print
print u"max level is:", max_level + 1
print u"level7 plus tuples:"
for (level, tup) in level7_plus_tups:
    print u"level:", level + 1, u"\ttup:", tup
print

