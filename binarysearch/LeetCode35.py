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
    
    # 自己写的
    @staticmethod
    def search_insert(nums: List[int], target: int) -> int:
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
    
    # 官方题解学的
    @staticmethod
    def search_insert_1(nums: List[int], target: int) -> int:
        low, high, ans = 0, len(nums) - 1, len(nums)
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans



if __name__ == '__main__':
    nums, target = [1, 3, 5, 6], 7
    s = Solution()
    print(s.search_insert(nums, target))
    print(s.search_insert_1(nums, target))
