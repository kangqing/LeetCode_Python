#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode441.py
@Time    :   2020/08/25 06:51:40
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode441 排列硬币
'''

# here put the import lib

class Solution441:
    def arrangeCoins(self, n: int) -> int:
        # [1, 2, 3.....k]
        # n个硬币，最小0行， 最大n行
        low, high = 0, n
        while low <= high:
            mid = (low + high) // 2
            count = self.getCount(mid)
            if count > n:
                high = mid - 1
            elif count < n:
                low = mid + 1
            else:
                return mid
        return high

    
    # 求mid行需要多少个硬币
    def getCount(self, mid: int) -> int:
        # a = list(range(mid + 1))
        # return sum(a)
        return ((mid + 1) * mid) // 2

if __name__ == '__main__':
    s = Solution441()
    print(s.arrangeCoins(8))