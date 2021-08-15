#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode233.py
@Time    :   2021/08/14 19:18:10
@Author  :   徐羕
@Contact :   ****@gmail.com
@Software:   VS Code
@Desc    :   LeetCode第233题
'''

# here put the import lib
class Solution:
    def countDigitOne(self, n: int) -> int:
        # k 个位开始分析
        ans, k = 0, 1
        # 12345  12340   5
        # 12300  45   10-19  
        while n >= k:
            pre = n // (k * 10) * k
            suf = max(n % (k * 10) - k + 1, 0)
            suf = min(suf, k)
            ans += (pre + suf)
            k *= 10
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.countDigitOne(12345))


