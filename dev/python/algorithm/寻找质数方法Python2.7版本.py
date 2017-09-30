
#!/usr/bin/python
# coding=utf8
# Find Primes
# Usage: ./findPrimes.py MAX

import sys

def findPrimes(max):
    """list findPrime(int max)
    
        返回找到的质数组成的列表.
    
        max为寻找的上限。"""
    primes = [2]

    for i in range(3, max):
        for j in primes:
            if i%j == 0:
                break
        else:
            primes.append(i)

    return primes

if __name__ == '__main__':

    MAX = int(sys.argv[1])
 
   print findPrimes(MAX)

    exit(0)