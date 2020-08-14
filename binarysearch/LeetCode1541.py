# -*- coding: utf-8 -*-
# @Time    : 2020/8/14 23:19
# @Author  : kangqing
# @Email   :  kangqing.37@gmail.com
# @File    : LeetCode1541.py
# @Software: PyCharm
# Solution1541 平衡括号字符串的最少插入次数
class Solution1541:
    # 不涉及类属性的操作建议设置为静态方法，方法中不需要加self
    @staticmethod
    def min_insertions(s: str) -> int:
        # 需要添加次数 左括号剩余数量 字符串长度 i自增数(相当于java中fori循环的i)
        ans, left, n, i = 0, 0, len(s), 0
        while i < n:
            if s[i] == '(':
                left += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 1
                else:
                    # 需要补一个右括号
                    ans += 1
                # 组合一个完整匹配的括号后需要给左括号减一
                if left > 0:
                    left -= 1
                else:
                    # 补一个左括号
                    ans += 1
            i += 1  # 每次i + 1
        ans += left * 2
        return ans


if __name__ == '__main__':
    solution1541 = Solution1541()
    print(solution1541.min_insertions(')))))))'))
