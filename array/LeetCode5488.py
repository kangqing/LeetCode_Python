# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 22:51
# @Author  : kangqing
# @Email   : kangqing.37@gmail.com
# @File    : LeetCode5488.py
# @Software: PyCharm
""" LeetCode5488 使数组中所有元素相等的最小操作数 """


class Solution:
    @staticmethod
    def min_operations(n: int) -> int:
        # 第一位数是1 最后一位是 2 * (n - 1) + 1 最后相同的值是 (first + last) / 2
        first, last = 1, 2 * (n - 1) + 1
        res = (first + last) // 2
        l = list([])
        d = 1
        while d < res:
            l.append(d)
            d += 2
        count = 0
        for x in l:
            count += res - x
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.min_operations(6))
