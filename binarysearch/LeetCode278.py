# -*- coding: utf-8 -*-
# @Time    : 2020/8/15 9:43
# @Author  : kangqing
# @Email   : kangqing.37@gmail.com
# @File    : LeetCode278.py
# @Software: PyCharm
"""
LeetCode278 第一个错误的版本
"""


class Solution278:
    import random
    x = random.randint(1, 1000)
    print('随机生成错误的版本开始为 = ', x)

    def first_bad_version(self, n):
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            b = self.is_bad_version(mid)
            # 如果当前版本错误，mid之后不可能为第一版错误，但是mid可能是
            if b:
                right = mid
            # 如果当前版本没错，错误只可能在mid + 1 到 你
            else:
                left = mid + 1
        return left

    # 检验当前版本是否是错误版本
    def is_bad_version(self, version):
        if version >= self.x:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution278()
    print('第一个错误的版本是 = ', s.first_bad_version(1000))
