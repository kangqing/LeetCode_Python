#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode000.py
@Time    :   2020/08/20 07:27:30
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode
'''

# here put the import lib
from typing import List
def nextGreatestLetter(letters: List[str], target: str) -> str:
    # 小写字母 = 97 - 122
    # 转换ASCII ord()
    index = 0
    low, high, length = 0, len(letters) - 1, len(letters) - 1
    while low < high:
        mid = (low + high) // 2
        if ord(letters[mid]) == ord(target):
            index = mid
        elif ord(letters[mid]) < ord(target):
            low = mid + 1
        else:
            high = mid - 1
    # 找到target应该在的位置
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


if __name__ == '__main__':
    print(nextGreatestLetter(['a', 'b', 'd'], 'a'))