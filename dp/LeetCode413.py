#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode413.py
@Time    :   2021/08/10 21:55:41
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   等差数列的顺序子序列
'''

# here put the import lib
from typing import List

"""
双指针解法：
x = 0开始，分别找到 3 个数的等差序列、4个数、5个数...直到不形成等差数列
然后 x + 1 继续寻找

"""
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for x in range(n - 2):
            d = nums[x + 1] - nums[x]
            for y in range(x + 1, n - 1):
                if nums[y + 1] - nums[y] == d:
                    ans += 1
                else:
                    break
        return ans

    
    """
    递归解法：
    """
    def number2(self, nums: List[int]) -> int:
        self.ans, n = 0, len(nums)
        self.digui(nums, n - 1)
        return self.ans

    def digui(self, nums: List[int], end: int) -> int:
        if end < 2:
            return 0
        op = 0
        # 如果以 end 为终点
        if nums[end] - nums[end - 1] == nums[end - 1] - nums[end - 2]:
            op = 1 + self.digui(nums, end - 1)
            self.ans += op
        else:
            self.digui(nums, end - 1)
        return op



    # 动态规划解法
    def number3(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for x in range(1, n - 1):
            if nums[x] - nums[x - 1] == nums[x + 1] - nums[x]:
                dp[x] = 1 + dp[x - 1]
        return sum(dp)