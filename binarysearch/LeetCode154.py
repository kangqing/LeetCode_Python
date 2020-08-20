
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode000.py
@Time    :   2020/08/20 15:59:07
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode154 寻找旋转排序数组中的最小值 II
'''

# here put the import lib

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        # 最后一个元素是一个特殊值x, 最小值右侧都 <= x, 最小值左侧都 >= x
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                # mid在最小值的左侧
                low = mid + 1
            elif nums[mid] < nums[high]:
                # mid在最小值的右侧
                high = mid
            else:
                # mid = high值得时候，不能判断在最小值左侧或者右侧
                # 但是 high 肯定 >= 最小值， 所以
                high -= 1
        return nums[low];



if __name__ == '__main__':
    s = Solution()
    arr = [10,2,10,10,10,10,10]
    print(s.findMin(arr))
