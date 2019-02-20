#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


if __name__ == '__main__':
    assert Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7, \
        Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])

    assert Solution().minPathSum([[1, 2, 5], [3, 2, 1]]) == 6, \
        Solution().minPathSum([[1, 2, 5], [3, 2, 1]])

    assert Solution().minPathSum([[1, 2], [5, 6], [1, 1]]) == 8, \
        Solution().minPathSum([[1, 2], [5, 6], [1, 1]])
