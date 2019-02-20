#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
并集查找
"""


class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        student_num = len(M)
        data = [i for i in range(student_num)]
        for i in range(student_num):
            for j in range(student_num):
                if M[i][j] == 1:
                    Solution.union(data, i, j)
        circle_num = 0
        for index in range(len(data)):
            if data[index] == index:
                circle_num += 1
        return circle_num

    @staticmethod
    def find(data, i):
        length = 0
        while data[i] != i:
            i = data[i]
            length += 1
        return data[i], length

    @staticmethod
    def union(data, i, j):
        if i == j:
            return
        root_i, length_i = Solution.find(data, i)
        root_j, length_j = Solution.find(data, j)
        if root_i == root_j:
            return
        if length_i < length_j:
            data[root_i] = data[root_j]
        else:
            data[root_j] = data[root_i]


if __name__ == '__main__':
    print(Solution().findCircleNum([[1, 0, 0, 1],
                                    [0, 1, 1, 0],
                                    [0, 1, 1, 1],
                                    [1, 0, 1, 1]]), 1)
    print(Solution().findCircleNum([[1, 1, 0],
                                    [1, 1, 0],
                                    [0, 0, 1]]), 2)
    print(Solution().findCircleNum([[1, 1, 0],
                                    [1, 1, 1],
                                    [0, 1, 1]]), 1)
