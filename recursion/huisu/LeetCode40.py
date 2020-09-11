#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode40.py
@Time    :   2020/09/11 16:04:14
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode40 组合总和 II
'''

# here put the import lib
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 排序是回溯法剪枝的前提，
        '''
        所谓剪枝，就是减去树的确定不可能符合条件的分支，以减少递归次数，增加代码的效率
        '''
        candidates.sort()
        res, length, stac = [], len(candidates), []
        self.hsf(candidates, target, 0, length, stac, res)
        return res
    
    def hsf(self, candidates: List[int], target: int, begin: int, length: int, stac: List[int], res: List[List[int]]):
        # 如果目标数被减为0说明能组合成目标数
        if target == 0:
            if list(stac) not in res:
                res.append(list(stac))
            return
        while begin < length:
            # 进行剪枝,此处去重
            if target - candidates[begin] < 0:
                break
            stac.append(candidates[begin])
            self.hsf(candidates, target - candidates[begin], begin + 1, length, stac, res)
            stac.pop()
            begin += 1


if __name__ == '__main__':
    s = Solution()
    res = s.combinationSum([10,1,2,7,6,1,5], 8)
    for x in res:
        print(x)