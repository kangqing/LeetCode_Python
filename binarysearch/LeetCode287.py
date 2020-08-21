
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode000.py
@Time    :   2020/08/21 07:41:00
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode287 寻找重复数
'''

# here put the import lib
from typing import List

'''
思路：
    这道题整体是牺牲空间换取时间的做法，现实中一般不会有这种要求
    重点在所有数都在 1 - n之间，这样一来就可以用 1 - n来二分
    遍历数组，看小于等于mid的数有几个，如果严格大于mid个，则重复数肯定在1 - mid
    否则在mid + 1 - n之间
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 分析，数字在1-n之间，则可以二分1-n,
        low, high = 1, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            count = 0
            for x in nums:
                if x <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicate([1,3,4,3,2]))