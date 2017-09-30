
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, array, target):
        if array == [[]]:
            return False
        nRow = len(array)
        nCol = len(array[0])
        if target < array[0][0] or target > array[nRow-1][nCol-1]:
            return False
        else:
            for i in range(nRow):
                for j in range(nCol):
                    if target == array[i][j]:
                        return True
            else:
                return False
            
a = Solution()
a.Find([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]],7)
