#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode4.py
@Time    :   2020/08/19 12:56:00
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode4 寻找两个正序数组的中位数
'''

# here put the import lib
from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        # 用nums2扩展nums1,相当于合并
        nums1.extend(nums2)
        # 排序
        nums1.sort()
        low, high = 0, len(nums1) - 1
        # 求中间数,长度为奇数直接返回，长度为偶数，则加上后一个数之后除以 2
        mid = (low + high) // 2
        if len(nums1) % 2 ==1:
            return nums1[mid]
        else:
            return (nums1[mid] + nums1[mid + 1]) / 2


if __name__ == '__main__':
    res = findMedianSortedArrays([1, 3], [2])
    print(res)
