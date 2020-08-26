#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode.py
@Time    :   2020/08/26 17:22:54
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode867 转置矩阵
'''

# here put the import lib
from typing import List
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        temp = []
        col = len(A[0])
        for i in range(col):
            for x in A:
                temp.append(x[i])
            res.append(temp.copy())
            temp.clear()
        return res


if __name__ == '__main__':
    s = Solution()
    a = s.transpose([[1,2,3],[4,5,6],[7,8,9]])
    print(a)