#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode200.py
@Time    :   2020/08/31 07:20:12
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode200 岛屿数量
'''

# here put the import lib
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        row, col, count = len(grid), len(grid[0]), 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1':
                    self.bfs(grid, x, y)
                    count += 1
        return count
    
    # 广度优先搜索
    def bfs(self, grid: List[List[str]], x: int, y: int):
        d = deque()
        d.append([x, y])
        # 当队列不为空
        while d:
            p = d.popleft()
            i, j = p[0], p[1]
            if 0 <= i and 0 <= j and i < len(grid) and j < len(grid[0]) and grid[i][j] == '1':
                # 访问过的陆地标记为 v 
                grid[i][j] = 'v'
                d.append([i - 1, j])
                d.append([i + 1, j])
                d.append([i, j - 1])
                d.append([i, j + 1])

    # 深度优先搜索
    def numIslands_dfs(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        row, col, count = len(grid), len(grid[0]), 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1':
                    count += 1
                    self.dfs(grid, x, y)
        return count
    
    def dfs(self, grid: List[List[str]], x: int, y: int):
        if x >=0 and y >= 0 and x < len(grid) and y < len(grid[x]) and grid[x][y] == '1':
            grid[x][y] = 'v'
            self.dfs(grid, x - 1, y)
            self.dfs(grid, x + 1, y)
            self.dfs(grid, x, y - 1)
            self.dfs(grid, x, y + 1)



if __name__ == '__main__':
    s = Solution()
    arr = [
            ['1','1','0','0','0'],
            ['1','1','0','0','0'],
            ['0','0','1','0','0'],
            ['0','0','0','1','1']
          ]
    # print(s.numIslands(arr))
    print(s.numIslands_dfs(arr))