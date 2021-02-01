#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   No8GridCount.py
@Time    :   2021/02/02 07:31:21
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   岛屿数量，广度优先搜索
'''

from typing import Deque, List
# here put the import lib
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 长宽
        row, col, count = len(grid), len(grid[0]), 0
        for i in range(row):
            for j in range(col):
                # 如果当前是土地才进行广度优先搜索
                if grid[i][j] == '1':
                    self.bfs(grid, i, j, row, col);
                    count += 1
        return count;


    def bfs(self, grid: List[List[str]], i: int, j: int, row: int, col: int) -> None:
        de = Deque()
        de.append([i, j])
        while de:
            po = de.pop()
            i, j = po[0], po[1]
            if i >= 0 and i < row and j >= 0 and j < col and grid[i][j] == '1':
                # 访问过得赋予一个其他值
                grid[i][j] = 'A'
                de.append([i, j + 1])
                de.append([i, j - 1])
                de.append([i + 1, j])
                de.append([i - 1, j])