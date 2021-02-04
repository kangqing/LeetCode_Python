#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   No3ThreeSum.py
@Time    :   2021/02/04 23:15:44
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   三数之和，双指针
'''


# here put the import lib
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()
        # 数组最后一位索引
        n = len(nums) - 1
        if n < 2:
            return []
        # 排序
        nums.sort()
        # 先找出第一位，再找剩下两位,从0到n-1，留两位余量
        for i in range(n - 1):
            # 最小的都大于0，肯定没有满足的
            if nums[0] > 0:
                break
            # 第一个数相同，跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 双指针找后两个数
            left, right, target = i + 1, n, -nums[i]
            while left < right:
                # 如果做指针 + 右指针 = target满足条件
                if nums[left] + nums[right] == target:
                    # 把三个数加入返回结果
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        # 等于上一个数则继续加
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        # 等于上一个数则继续减
                        right -= 1
                elif nums[right] + nums[left] > target:
                    right -= 1
                else:
                    left += 1
        return res;
                    

if __name__ == '__main__':
    s = Solution()
    list = s.threeSum([-1,0,1,2,-1,-4])
    print(list)





