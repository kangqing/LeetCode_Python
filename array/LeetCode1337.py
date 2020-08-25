#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode1337.py
@Time    :   2020/08/25 19:49:07
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode1337 方阵中战斗力最弱的 K 行
'''

# here put the import lib
from typing import List
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # row, col = len(mat), len(mat[0])
        jun = list([])
        for x in mat:
            # 统计1在列表中出现的次数
            count = x.count(1)
            jun.append(count)
        res = list([])
        #复制一个列表并排序
        jun_copy = jun.copy()
        jun_copy.sort()
        # 用排好序的战力值去没排序的列表找位置
        for x in jun_copy:
            if len(res) == k:
                break
            index = jun.index(x)
            res.append(index)
            # 使用过的位置赋值-1，不会再次被取到
            jun[index] = -1
        return res


if __name__ == '__main__':
    s = Solution()
    arr = [[1,1,0,0,0],
           [1,1,1,1,0],
           [1,0,0,0,0],
           [1,1,0,0,0],
           [1,1,1,1,1]]
    print(s.kWeakestRows(arr, 3))