#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   No1MaxSubSum.py
@Time    :   2020/08/29 23:53:05
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   2020名企高频 最大子序和
'''
from typing import List
# 动态规划，转移方程 dp[i] = max(dp[i - 1] + nums[i], nums[i])
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


if __name__ == '__main__':
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    print(s.maxSubArray(arr))
