#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode719.py
@Time    :   2020/08/22 07:35:44
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode719 找出第 k 小的距离对
'''

# here put the import lib
from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        # 最小距离肯定是0
        # 最大距离是nums[-1] - nums[0]
        low, high = 0, nums[-1] - nums[0]
        # 二分法
        while low < high:
            mid = (low + high) // 2
            # 调用方法求出count
            count = self.query_count(nums, mid)
            # 若小于mid的距离差总数 >= k，则距离差应落在 [low, mid] 之间
            # 若大于mid的距离差总数 < k，则距离差应落在 [mid+1, high] 之间
            if count >= k:
                high = mid
            else:
                low = mid + 1
        return low


    
    #查询小于等于 mid 值得距离的数量
    def query_count(self, nums: List[int], mid: int) -> int:
        # 快慢指针, 计数器
        slow, count = 0, 0
        # 快指针指着索引为1的位置，直到最后len(nums) - 1 的位置
        for fast in range(1, len(nums)):
            # 当快指针值 -  慢指针值 > mid中位数
            while nums[fast] - nums[slow] > mid:
                # 给慢指针加一
                slow += 1
            # 统计当快指针为fast的时候距离小于等于mid值得数量
            count += fast - slow
        return count


if __name__ == '__main__':
    s = Solution()
    arr = [1, 1, 1, 2, 2, 3]
    k = 8
    print(s.smallestDistancePair(arr, k))