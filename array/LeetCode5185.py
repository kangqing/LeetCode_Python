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

    @staticmethod
    def three_consecutive_odds_1(arr: List[int]) -> bool:
        coll = list([])
        for x in arr:
            if x % 2 == 1:
                coll.append(x)
                if len(coll) == 3:
                    return True
            else:
                coll.clear()       
        return False


if __name__ == '__main__':
    s = Solution()
    d = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    print(s.three_consecutive_odds(d))
    print(s.three_consecutive_odds_1(d))

