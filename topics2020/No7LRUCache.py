#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   No7LRUCache.py
@Time    :   2021/02/01 15:58:52
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LRU最近最少使用
'''

# here put the import lib

class Node:
    def __init__(self, k = 0, v = 0):
        self.k = k
        self.v = v
        self.p = None
        self.n = None

class LRUCache:


    def __init__(self, capacity: int):
        self.map = dict()
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.n = self.tail
        self.tail.p = self.head

    def get(self, key: int) -> int:
        # 不存在则返回 -1
        if key not in self.map:
            return -1;
        # 如果存在，先通过hash表找到，然后移动到结尾，代表最近使用了
        node = self.map[key]
        self.moveToTail(node)
        return node.v


    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            # 证明不存在
            # 新建此节点
            node = Node(key, value)
            self.map[key] = node
            # 添加到尾部
            self.addToTail(node)
            if len(self.map) > self.capacity:
                # 证明容量不够了，需要删除头结点
                node = self.removeHead()
                del self.map[node.k]
        else:
            # 存在
            node = self.map[key]
            node.v = value
            self.moveToTail(node)

    

    # 添加节点到结尾
    def addToTail(self, node: Node) -> None:
        node.p = self.tail.p
        node.n = self.tail
        self.tail.p = node
        self.tail.p.n = node
    

    # 移动节点到结尾
    def moveToTail(self, node: Node) -> None:
        self.removeNode(node)
        self.addToTail(node)

    # 删除任意节点
    def removeNode(self, node: Node) -> None:
        node.p.n = node.n
        node.n.p = node.p
    
    # 删除头结点，头结点为最近最少使用节点
    def removeHead(self) -> Node:
        node = self.head.n
        self.removeNode(node)
        return node

if __name__ == '__main__':
    a = LRUCache(2)
    print(a.get(1))
    print(a.put(1, 1))
    print(a.put(1, 2))
    print(a.put(2, 1))
    print(a.put(4, 1))
    print(a.get(2))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)