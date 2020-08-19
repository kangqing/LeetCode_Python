#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode000.py
@Time    :   2020/08/19 11:27:30
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode658 找到 K 个最接近的元素
'''

# here put the import lib


from typing import List
def query(nums: List[int], k: int, target: int) -> List[int]:
    n, res = len(nums), list([])
    ind = find_index(nums, target)
    if ind == 0:
        res = nums[ : k]
    else:
        # 不在首位，也不在末尾，则需要再次判断
        lt, rt = ind - 1, ind
        if ind == n:
            rt = n - 1
        while len(res) < k:
            if abs(nums[lt] - target) <= abs(nums[rt] - target):
                res.append(nums[lt])
                if lt - 1 >= 0:
                    lt -= 1
                else:
                    # 直接取右边的值
                    n = k - len(res)
                    if n ==0:
                        break
                    res.extend(nums[rt : rt + n])
            else:
                res.append(nums[rt])
                if rt + 1 < n:
                    rt += 1
                else:
                    # 直接取左边的值
                    n = k - len(res)
                    if n == 0:
                        break
                    res.extend(nums[lt - n + 1 : lt + 1])
        res.sort()
    return res




# 先找出target应该所在位置的索引
def find_index(nums: List[int], target: int) -> int:
    low, high, ind = 0, len(nums) - 1, len(nums)
    while low <= high:
        mid = (low + high) // 2
        if target <= nums[mid]:
            ind = mid
            high = mid - 1
        else:
            low = mid + 1
    return ind


if __name__ == '__main__':
    print(query([1,1, 1, 1,2 ,3,4,5,7,8,9], 8, 2))
