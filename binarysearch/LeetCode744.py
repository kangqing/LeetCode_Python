#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode000.py
@Time    :   2020/08/20 07:27:30
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode744 寻找比目标字母大的最小字母
'''

# here put the import lib
from typing import List
class Solution:
    # 自己写的方法，比较笨
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 小写字母 = 97 - 122
        # 转换ASCII ord()
        index = 0
        low, high, length = 0, len(letters) - 1, len(letters) - 1
        # 找到target应该在的位置
        while low <= high:
            mid = (low + high) // 2
            if ord(target) <= ord(letters[mid]):
                index = mid
                high = mid - 1
            else:
                low = mid + 1
        # 分析index位置
        if index == len(letters):
            index = 0
        else:
            while index < length and letters[index] == target:
                index += 1
            if index == length and letters[index] == target:
                index = 0
            else:
                pass
        return letters[index]

    # 照着官方题解的方法
    def nextGreatestLetter_1(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters)
        # 求出要插入target到列表中应该插入到的位置
        while low < high:
            mid = (low + high) // 2
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid
        # 巧妙的运用取模找到对应结果
        return letters[low % len(letters)]

if __name__ == '__main__':
    s = Solution()
    arr, target = ["c","f","j"], 'v'
    print(s.nextGreatestLetter(arr, target))
    print(s.nextGreatestLetter_1(arr, target))