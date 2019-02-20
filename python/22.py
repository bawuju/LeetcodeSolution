#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Solution:

    @staticmethod
    def append_left(result, counter, remaining):
        if counter == 0 and remaining == 0:
            return [result]
        if remaining == 0:
            return [result + ')' * counter]
        if counter == 0:
            return Solution.append_left(result + '(', counter + 1, remaining - 1)
        r1 = Solution.append_left(result + '(', counter + 1, remaining - 1)
        r2 = Solution.append_left(result + ')', counter - 1, remaining)
        return r1 + r2

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return Solution.append_left('(', 1, n - 1)


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
