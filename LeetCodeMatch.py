""" 力扣周赛专用 """
from typing import List


class SolutionMatch:
    """ 力扣周赛专用类 """
    def thousandSeparator(self, n: int) -> str:
        s = "{:,}".format(n)
        res = ""
        for x in s:
            if x == ',':
                res += '.'
            else:
                res += x
        return res

if __name__ == '__main__':
    s = SolutionMatch()

    n = 10000000
    print(s.thousandSeparator(n))
