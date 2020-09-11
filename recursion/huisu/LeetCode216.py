#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode216.py
@Time    :   2020/09/11 16:38:54
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode216 组合总和 III
'''

# here put the import lib
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 排序是回溯法剪枝的前提，
        '''
        所谓剪枝，就是减去树的确定不可能符合条件的分支，以减少递归次数，增加代码的效率
        '''
        res, stac, candidates = [], [], [1,2,3,4,5,6,7,8,9]
        self.hsf(candidates, n, 0, k, stac, res)
        return res
    
    def hsf(self, candidates: List[int], n: int, begin: int, k: int, stac: List[int], res: List[List[int]]):
        # 如果目标数被减为0说明能组合成目标数
        if n == 0:
            if len(stac) == k:
                res.append(list(stac))
            return
        while begin < len(candidates):
            # 进行剪枝
            if n - candidates[begin] < 0:
                break
            stac.append(candidates[begin])
            self.hsf(candidates, n - candidates[begin], begin + 1, k, stac, res)
            stac.pop()
            begin += 1


if __name__ == '__main__':
    s = Solution()
    res = s.combinationSum3(3, 7);
    for x in res:
        print(x)