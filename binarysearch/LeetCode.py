# -*- coding: utf-8 -*-
# @Time    : 2020/8/14 6:33
# @Author  : kangqing
# @Email   :  kangqing.37@gmail.com
# @File    : LeetCode.py
# @Software: PyCharm
import random


# python没有自增自减操作 i++, ++i 和 i--, --i都是不对的
class LeetCode:
    # python只有类变量和实例变量的概念，没有静态变量的概念，这里x是类变量
    x = random.randint(1, 1000)
    print('自动生成的数字是 = ', x)

    # 猜测数字如果规定数字<=>num分别返回-1、0、1
    def guess(self, num: int) -> int:
        if num == self.x:
            return 0
        elif num < self.x:
            return -1
        else:
            return 1

    # 猜数字的函数
    def guess_number(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            res = self.guess(mid)
            if res == 0:
                return mid
            elif res < 0:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# main函数
if __name__ == '__main__':
    leetcode374 = LeetCode()
    print('代码猜测结果是', leetcode374.guess_number(1000))
