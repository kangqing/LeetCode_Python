#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode35.py
@Time    :   2020/08/18 11:30:37
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode35 搜索插入位置
'''

# here put the import lib
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        low, high = 0, len(nums) -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                if mid > 0 and nums[mid - 1] < target:
                    return mid
                else:
                    high = mid - 1

        return low


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 1))