#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode77.py
@Time    :   2020/09/08 07:36:05
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode77 组合
'''

# here put the import lib
from typing import List

'''
经典回溯法解法
先选一个数字，然后进入递归继续选，满足条件后加到结果中，然后回溯到上一步，继续递归
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = []
        self.getAns(1, n, k, temp, res)
        return res

    def getAns(self, start: int, n: int, k: int, temp: List[int], res: List[List[int]]):
        # 如果 temp 里的数字够了 k 个，就把它加入到结果中
        # 注意新建一个加到结果中
        if len(temp) == k:
            t = list(temp)
            res.append(t)
            return
        # 从 start 到 n
        for i in range(start, n + 1):
            # 将当前数字加入 temp
            temp.append(i)
            # 进入递归
            self.getAns(i + 1, n, k , temp, res)
            # 删除当前数字，进入下次 for 循环
            temp.pop(len(temp) - 1)

if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 3))