""" 力扣周赛专用 """
from typing import List


class SolutionMatch:
    """ 力扣周赛专用类 """


    # 441
    def arrangeCoins(self, n: int) -> int:
        res = 0
        if n < 2:
            return n
        # [1, 2, 3.....k]
        # n个硬币，最小0行， 最大n行
        low, high = 0, n
        while low <= high:
            mid = (low + high) // 2
            count = self.getCount(mid)
            if count > n:
                high = mid - 1
            elif count < n:
                low = mid + 1
            else:
                res = mid
        res = high
        return res

    
    # 求mid行需要多少个硬币
    def getCount(self, mid: int) -> int:
        a = list(range(mid + 1))
        return sum(a)

if __name__ == '__main__':
    s = SolutionMatch()

    print(s.arrangeCoins(3))
