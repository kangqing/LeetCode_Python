'''
Author: your name
Date: 2020-08-17 06:24:55
LastEditTime: 2020-08-27 07:29:55
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \LeetCode_Python\LeetCodeMatch.py
'''
""" 力扣周赛专用 """
from typing import List
import heapq
import collections


class SolutionMatch:
    """ 力扣周赛专用类 """
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(curr: str):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)

        vec = collections.defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapq.heapify(vec[key])
        
        stack = list()
        dfs("JFK")
        return stack[::-1]


if __name__ == '__main__':
    s = SolutionMatch()
    print(s.findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]))
