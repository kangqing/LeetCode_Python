#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode133.py
@Time    :   2020/10/20 09:37:39
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode133 重排链表
'''

# here put the import lib


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int, next:None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        mylist = []
        while head is not None:
            mylist.append(head)
            head = head.next
        left, right = 0, len(mylist) - 1
        while left < right:
            mylist[left].next = mylist[right]
            left += 1
            if left == right:
                break
            mylist[right].next = mylist[left]
            right -= 1
        mylist[right].next = None

if __name__ == "__main__":
    node = ListNode(1, None)
    node2 = node.next = ListNode(2, None)
    node3 = node2.next = ListNode(3, None)
    node4 = node3.next = ListNode(4, None)

    s = Solution()
    s.reorderList(node)
