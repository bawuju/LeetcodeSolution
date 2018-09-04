#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return Solution.inner_num_trees(n, [0] * (n + 1))

    @staticmethod
    def inner_num_trees(length, tmp):
        if tmp[length] > 0:
            return tmp[length]
        if length <= 2:
            return length
        counter = 0
        for index in range(length):
            left_length = index
            right_length = length - index - 1
            left_count = Solution.inner_num_trees(left_length, tmp)
            right_count = Solution.inner_num_trees(right_length, tmp)
            counter += (max(1, left_count) * max(1, right_count))
        tmp[length] = counter
        return counter


if __name__ == '__main__':
    print(Solution().numTrees(3))
