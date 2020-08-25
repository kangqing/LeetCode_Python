'''
Author: your name
Date: 2020-08-17 06:24:55
LastEditTime: 2020-08-26 07:58:19
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \LeetCode_Python\LeetCodeMatch.py
'''
""" 力扣周赛专用 """
from typing import List


class SolutionMatch:
    """ 力扣周赛专用类 """
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
    s = SolutionMatch()
    print(s.letterCombinations('2'))
