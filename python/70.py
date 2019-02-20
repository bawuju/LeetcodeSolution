#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        tmp = [i + 1 for i in range(n)]
        for i in range(2, n):
            tmp[i] = tmp[i - 1] + tmp[i - 2]
        return tmp[-1]


if __name__ == '__main__':
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
