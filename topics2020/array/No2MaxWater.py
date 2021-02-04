#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   No2MaxWater.py
@Time    :   2021/02/04 20:59:23
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   盛最多水的容器
'''

from typing import List
# here put the import lib
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 最大盛水量，左指针， 右指针
        count, left, right = -1, 0, len(height) - 1
        lvalue, rvalue = height[0], height[len(height) - 1]
        while left < right:
            count = max(count, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
                while left < right and height[left] <= lvalue:
                    left += 1
                lvalue = height[left]
            else:
                right -= 1
                while left < right and height[right] <= rvalue:
                    right -= 1
                rvalue = height[right]
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))