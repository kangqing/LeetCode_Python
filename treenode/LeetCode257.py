#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode257.py
@Time    :   2020/09/04 07:33:09
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode257 二叉树的所有路径
'''

# here put the import lib
from typing import List

class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

# 深度优先搜索
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root: TreeNode, path:str, paths: List[str]):
        if root:
            path += str(root.val)
            if not root.left and not root.right:
                paths.append(path)
            else:
                # 否则不是叶子结点，继续递归遍历
                path += "->"
                if root.left:
                    self.dfs(root.left, path, paths)
                if root.right:
                    self.dfs(root.right, path, paths)
