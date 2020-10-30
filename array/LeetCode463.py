#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode463.py
@Time    :   2020/10/30 17:38:17
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode463 岛屿的周长
'''

# here put the import lib
from typing import List

def get0Count(grid: List[List[int]], i:int, j:int, row:int, col:int) -> int:
        res = 0
        if i - 1 < 0:
            res += 1
        else:
            if grid[i - 1][j] == 0:
                res += 1
        if i + 1 == row:
            res += 1
        else:
            if grid[i + 1][j] == 0:
                res += 1
        if j - 1 < 0:
            res += 1
        else:
            if grid[i][j - 1] == 0:
                res += 1
        if j + 1 == col:
            res += 1
        else:
            if grid[i][j + 1] == 0:
                res += 1
        return res

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 行， 列
        row, col, res = len(grid), len(grid[0]), 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    continue
                if grid[i][j] == 1:
                    # 计算周围水域数量
                    res += get0Count(grid, i, j, row, col)
        return res


if __name__ == "__main__":
    for i in range(5):
        print(i)