#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode17.py
@Time    :   2020/08/26 17:29:44
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode17 电话号码的字母组合
'''

# here put the import lib
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {}
        dict['2'] = 'abc'
        dict['3'] = 'def'
        dict['4'] = 'ghi'
        dict['5'] = 'jkl'
        dict['6'] = 'mno'
        dict['7'] = 'pqrs'
        dict['8'] = 'tuv'
        dict['9'] = 'wxyz'
        if len(digits) == 1:
            return list(dict[digits])
        res = list([])
        length = len(digits)
        index = 0
        while index < length - 1:
            x = digits[index]
            next = digits[index + 1]
            index += 1
            d1 = dict[x]
            if len(res) > 0:
                d1 = res.copy()
                res.clear()
            d2 = dict[next]
            for i in d1:
                for j in d2:
                    res.append(i + j)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))