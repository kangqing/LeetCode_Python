# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 22:33
# @Author  : kangqing
# @Email   : kangqing.37@gmail.com
# @File    : LeetCode5185.py
# @Software: PyCharm
""" LeetCode5185 存在连续三个奇数的数组 """
from typing import List


class Solution:
    @staticmethod
    def three_consecutive_odds(arr: List[int]) -> bool:
        i, n = 1, len(arr)
        if n < 3:
            return False
        while i < n - 1:
            if arr[i] % 2 != 1:
                i += 1
                continue
            if arr[i - 1] % 2 != 1:
                i += 1
                continue
            if arr[i + 1] % 2 != 1:
                i += 1
                continue
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.three_consecutive_odds([1, 2, 34, 3, 4, 5, 7, 23, 12]))

