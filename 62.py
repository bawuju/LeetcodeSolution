#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        tmp = [[0] * n for i in range(m)]
        for i in range(m):
            tmp[i][0] = 1
        for i in range(n):
            tmp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                tmp[i][j] = tmp[i - 1][j] + tmp[i][j - 1]
        return tmp[-1][-1]


if __name__ == '__main__':
    assert Solution().uniquePaths(7, 3) == 28, Solution().uniquePaths(7, 3)
    assert Solution().uniquePaths(23, 12) == 193536720, Solution().uniquePaths(23, 12)
