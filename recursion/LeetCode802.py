#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode802.py
@Time    :   2021/08/05 22:44:15
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode802 找到最终的安全状态
'''

# here put the import lib
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n

        def safe(x: int) -> bool:
            if color[x] > 0:
                return color[x] == 2
            color[x] = 1
            for i in graph[x]:
                if not safe(i):
                    return False
            color[x] = 2
            return True
        
        return [i for i in range(n) if safe(i)]
