#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode212.py
@Time    :   2020/09/02 06:08:10
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode752 打开转盘锁
'''

# here put the import lib
from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        count = 0
        # 设置一个set集合，防止重复转动
        s = set()
        d = deque()
        # 初始值入队列
        d.append('0000')
        s.add('0000')
        while d:
            n = len(d)
            # 每次都把队列中的数转动一遍
            for i in range(n):
                currStr = d.popleft()
                if currStr == target:
                    return count
                if currStr in deadends:
                    continue
                # 转盘锁4个位置向上或者向下转动一下
                for x in range(4):
                    a = self.up_or_dowm_lock(currStr, True, x)
                    b = self.up_or_dowm_lock(currStr, False, x)
                    if a not in s:
                        s.add(a)
                        d.append(a)
                    if b not in s:
                        s.add(b)
                        d.append(b)
            count += 1
        return -1
        
    # 把转盘锁某个位置向上或者向下转动一位
    def up_or_dowm_lock(self, currStr: str, isUp: bool, ind: int) -> str:
        curr = list(currStr)
        if isUp:
            if curr[ind] == '9':
                curr[ind] = '0'
            else:
                curr[ind] = chr(ord(curr[ind]) + 1)
        else:
            if curr[ind] == '0':
                curr[ind] = '9'
            else:
                curr[ind] = chr(ord(curr[ind]) - 1)
        return ''.join(curr)


if __name__ == '__main__':
    s = Solution()
    print(s.openLock(["0201","0101","0102","1212","2002"], '0202'))