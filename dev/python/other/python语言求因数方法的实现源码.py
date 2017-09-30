
#coding:utf-8

import math

def generator(count, s):
    if count == 1:
        for i in s:
            yield i
    else:
        for i in s:
            _ = set(s)
            _.remove(i)
            for _ in generator(count-1, _):
                yield _ * 10 + i

primes = [2, 3]
def prime(idx):
    if idx < len(primes):
        return primes[idx]
    new = primes[-1]+2
    while True:
        for i in primes:
            if new % i == 0:
                break
        else:
            primes.append(new)
            break
        new += 2
    return prime(idx)

def probe(number, idx, value=0):
    if value > number:
        return value
    p = prime(idx)
    sqrt = math.sqrt(number)
    while number % p != 0 and sqrt >= p:
        idx += 1
        p = prime(idx)
    if sqrt < p:
        return number
    return probe(number/p, idx, max(p, value))

#www.iplaypy.com

if __name__ == '__main__':
    _min = 10000000000, 10000000000
    _max = 0, 0
    for number in generator(9, set(range(1, 10))):
        maxfactor = probe(number, 0)
        if maxfactor < _min[0]:
            _min = maxfactor, [number]
        elif maxfactor == _min[0]:
            _min[1].append(number)
        if maxfactor > _max[0]:
            _max = maxfactor, [number]
        elif maxfactor == _max[0]:
            _max[1].append(number)
    print _min
    print _max

