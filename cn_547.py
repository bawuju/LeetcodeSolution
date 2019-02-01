#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
只是递归扫描并标记已经被扫描过的，没啥特殊
要注意的是一个人只和自己作为朋友，也可以成为一个朋友圈
"""


class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        tmp = []
        student_num = len(M)
        for i in range(student_num):
            tmp.append([])
            for j in range(student_num):
                tmp[i].append(False)
        circle_num = 0
        for i in range(student_num):
            for j in range(student_num):
                if tmp[i][j]:
                    continue
                if M[i][j] == 1:  # 如果i和j是朋友，并且没有被扫描过，那就从这两个人的关系开始扫描
                    circle_num += 1
                    Solution.scan(M, tmp, i)
                    Solution.scan(M, tmp, j)
        return circle_num

    @staticmethod
    def scan(M, tmp, i):
        student_num = len(M)
        for target_j in range(student_num):  # 扫描每一个人，判断他跟i是不是朋友，如果是的话，递归扫描下去
            if M[i][target_j] == 1 and not tmp[i][target_j]:
                # 朋友关系是相互的
                tmp[i][target_j] = True
                tmp[target_j][i] = True
                Solution.scan(M, tmp, target_j)


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
