#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode410.py
@Time    :   2020/08/22 21:22:43
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode410 分割数组的最大值
'''

# here put the import lib
from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 二分法的两个边界
        # 最小的是每个数分一个组，取最大值的，最大即为不分组
        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low + high) // 2
            # 使用mid作为分组之后的最大值进行分组
            count = self.group(nums, mid)
            # 如果组数 > m 说明：mid小了，所以分组多了
            if count > m:
                low = mid + 1
            else:
                high = mid
        return low

    #  计算分为最大数为mid的时候分的组数， 显然mid越大，分出的组数越少
    def group(self, nums: List[int], mid: int) -> int:
        # 最少一组， 和为0
        count, sum = 1, 0
        for x in nums:
            if sum + x > mid:
                # 组数加一需要重新分组
                count += 1
                # 数组和置为此数
                sum = x
            else:
                sum += x
        return count
