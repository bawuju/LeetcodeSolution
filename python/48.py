#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for start in range(len(matrix) // 2):
            Solution.inner_swap(matrix, start)

    @staticmethod
    def inner_swap(matrix, start):
        size = len(matrix) - start * 2
        length = len(matrix)
        for index in range(start, start + size - 1):
            line, column = start, index
            tmp = matrix[line][column]
            for counter in range(4):
                line, column = column, length - 1 - line
                matrix[line][column], tmp = tmp, matrix[line][column]


def test(target):
    Solution().rotate(target)
    for t in target:
        print(t)
    print()


if __name__ == '__main__':
    test([
        [1, 2],
        [3, 4]
    ])
    test([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    test([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])
