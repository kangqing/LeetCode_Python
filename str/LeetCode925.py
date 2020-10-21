#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode925.py
@Time    :   2020/10/21 15:11:21
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode925 长按键入
'''

# here put the import lib
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while j < len(typed):
            if i < len(name) and typed[j] == name[i]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == len(name)


if __name__ == "__main__":
    s = Solution()
    print(s.isLongPressedName("aaacv", 'a'))
