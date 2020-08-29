#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode214.py
@Time    :   2020/08/29 23:53:05
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode214 最短回文子串
'''

# here put the import lib
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        f = s[::-1]
        n = len(s)
        for x in range(n):
            if f[x:n] == s[0:n-x]:
                return f + s[n-x:n]
        return f


if __name__ == '__main__':
    s = Solution()
    print(s.shortestPalindrome('abcd'))