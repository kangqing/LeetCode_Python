#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LeetCode714.py
@Time    :   2020/12/17 14:08:10
@Author  :   kangqing
@Contact :   kangqing.37@gmail.com
@Software:   VS Code
@Desc    :   LeetCode714 买卖股票的最佳时机含手续费
'''

# here put the import lib
from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 分析转移方程
        # d[i][0] 代表第i天手中无股票
        # d[i][1] 代表第i天手中有股票

        # d[i][0] = math.max(d[i - 1][0], d[i - 1][1] + prices[i] - fee)
        # 解释：第i天手中无股票 必定从昨天手中无股票 或者 昨天有股票 + 卖出今天 - 手续费 转移而来
        # d[i][1] = math.max(d[i - 1][1], d[i - 1][0] - prices[i])
        # 解释： 第i天手中有股票 必定从昨天手中有一股票 或者昨天无股票 - 今天买入股票 转移而来

        # 分析最佳收益肯定是 d[n - 1][0]
        n = len(prices)
        sell, buy = 0, -prices[0]
        for i in range(1, n):
            sell, buy = max(sell, buy + prices[i] - fee), max(buy, sell - prices[i])
        return sell;


if __name__ == "__main__":
    s = Solution()
    list = [1, 3, 2, 8, 4, 9]
    print(s.maxProfit(list, 2))