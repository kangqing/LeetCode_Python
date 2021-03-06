#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode162.py
@Time    :   2020/08/17 09:47:13
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode162 寻找峰值
'''

# here put the import lib
from typing import List


"""
思路：二分查找
1.任何一个位置的的mid索引处的值 < mid索引处的值， 那么峰值只可能在当前节点右面
2.反之则有可能在当前节点或者当前节点左边
3.知道不满足left < right为止，left节点则为峰值
"""


class Solution:
    @staticmethod
    def find_peak_element(nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.find_peak_element([1, 2, 1, 3, 5, 6, 4]))
