""" 力扣周赛专用 """
from typing import List


class SolutionMatch:
    """ 力扣周赛专用类 """
    def shortestPalindrome(self, s: str) -> str:
        f = s[::-1]
        n = len(s)
        for x in range(n):
            if f[x:n] == s[0:n-x]:
                return f + s[n-x:n]
        return f

if __name__ == '__main__':
    s = SolutionMatch()
    print(s.shortestPalindrome('1234'))