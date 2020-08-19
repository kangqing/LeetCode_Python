#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   QuickSort.py
@Time    :   2020/08/19 17:53:26
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   快速排序
'''

# here put the import lib

from typing import List

class QuickSort:

    def quick_sort(self, arr: List[int], low: int, high: int):
        if low < high:
            index = self.get_index(arr, low, high)
            # 递归基准值左边
            self.quick_sort(arr, low, index - 1)
            # 递归基准值右边
            self.quick_sort(arr, index + 1, high)

    # 调整顺序并获取基准值的位置
    def get_index(self, arr: List[int], low: int, high: int) -> int:
        # 定义第一个数为基准值
        temp = arr[low]
        while low < high:
            # 尾指针从后往前找，找到小于基准数的位置停下
            while arr[high] >= temp and low < high:
                high -= 1
            # 找到之后移动到基准数的位置
            arr[low] = arr[high]
            # 头指针从头往后找大于基准数的位置停下
            while arr[low] <= temp and low < high:
                low += 1
            # 找到之后移动到 high位置,
            # 到这里相当于一个小于基准数的数 和 一个大于基准数的数 互换位置
            arr[high] = arr[low]
        
        # 跳出循环时候 low = high, 此时将基准值赋给这个位置
        arr[low] = temp 
        # 返回基准值的位置
        return low

# main测试快速排序
if __name__ == '__main__':
    q = QuickSort()
    arr = [3, 5, 1, 12, 6, 2, 10, 8, 3, 5]
    low, high = 0, len(arr) - 1
    q.quick_sort(arr, low, high)
    print(arr)