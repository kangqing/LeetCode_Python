#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode279.py
@Time    :   2020/09/17 14:19:31
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode279 完全平方数
'''

# here put the import lib
import math

'''

动态规划
动态规划
求组成目标数字的最小数量
[1, 4] 组成目标的值
target = 7
f(7) = f(7 - 1) + 1次
f(7) = f(7 - 4) + 1次
f(7) = Math.min(f(7 - 1) + 1, f(7 - 4) + 1)
以此类推
f(0) = 0次是已知

'''
class Solution:
    def numSquares(self, n: int) -> int:
        # 计算出<=目标数的完全平方数
        list = []
        max_ind = int(math.sqrt(n)) + 1
        for i in range(max_ind):
            list.append(i * i)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for x in range(1, n + 1):
            for y in list:
                if x < y:
                    break
                dp[x] = min(dp[x], dp[x - y] + 1)
        return int(dp[-1])


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(7))