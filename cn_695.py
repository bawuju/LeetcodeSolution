#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


"""
图的遍历
"""


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        tmp = []
        for i in range(len(grid)):
            tmp.append([])
            for j in range(len(grid[0])):
                tmp[i].append(False)
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if tmp[i][j]:
                    continue
                if grid[i][j] == 0:
                    tmp[i][j] = True
                    continue
                stack = [[i, j]]
                current_area = 0
                while stack:
                    row, column = stack.pop()
                    if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]):
                        continue
                    if tmp[row][column]:
                        continue
                    tmp[row][column] = True
                    if grid[row][column] == 0:
                        continue
                    current_area += 1
                    stack.append([row + 1, column])
                    stack.append([row - 1, column])
                    stack.append([row, column + 1])
                    stack.append([row, column - 1])
                max_area = max(max_area, current_area)
        return max_area


if __name__ == '__main__':
    print(Solution().maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                      [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                      [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]), 6)
    print(Solution().maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]), 0)
