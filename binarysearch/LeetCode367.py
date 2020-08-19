#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode367.py
@Time    :   2020/08/19 22:30:25
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode367 有效的完全平方数
'''

# here put the import lib
def isPerfectSquare(num: int) -> bool:
    if num == 1:
        return True
    # 二分法的tail = num // 2因为一个数开平方肯定 <= 他的一半
    head, tail = 2, num // 2
    while head <= tail:
        mid = (head + tail) // 2
        d = mid * mid
        if d == num:
            return True
        elif d < num:
            head = mid + 1
        else:
            tail = mid - 1
    return False


if __name__ == '__main__':
    print(isPerfectSquare(16))