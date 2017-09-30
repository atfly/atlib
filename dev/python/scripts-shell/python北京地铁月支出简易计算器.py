
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import math

#  0-100 *1
#  100< <=150 *0.8
#  150<       *0.5
def caclMonthFee(perPrice):
    totalTimes=22*2
    firstTimes = math.ceil(100/perPrice)
    secondTimes = math.ceil(50/(perPrice*0.8))
    if (firstTimes + secondTimes > totalTimes):
        secondTimes = (totalTimes -firstTimes)
        thirdTimes=0
    else:
        thirdTimes = totalTimes-int(firstTimes)-int(secondTimes)
    total=firstTimes*perPrice+secondTimes*perPrice*0.8+thirdTimes*perPrice*0.5
    return total

if __name__ == '__main__':
    print("单次票价, 月支出,  年支出")
    for i in range(3,9):
        perMonth =caclMonthFee(i)
        print(i, perMonth, round(perMonth*12,1))

