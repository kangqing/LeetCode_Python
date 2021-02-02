#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   No1DoubleArrMid.py
@Time    :   2021/02/03 07:11:31
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   寻找两个正序数组的中位数
'''

from typing import List
# here put the import lib
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 把 nums2 扩展至 nums1 后面
        nums1.extend(nums2)
        # 排序
        nums1.sort()
        low, high = 0, len(nums1) - 1
        mid = (low + high) // 2
        if len(nums1) % 2 == 1:
            return nums1[mid]
        else:
            return (nums1[mid] + nums1[mid + 1]) / 2


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([2, 4], [1, 3]))