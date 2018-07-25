#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class GeneratePermutation:
    @staticmethod
    def generate(start, end, ex=None):
        pass


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pass


if __name__ == '__main__':
    print(GeneratePermutation.generate(1, 9))
    assert Solution().nextPermutation([1, 2, 3]) == [1, 3, 2], Solution().nextPermutation([1, 2, 3])
    assert Solution().nextPermutation([3, 2, 1]) == [1, 2, 3], Solution().nextPermutation([3, 2, 1])
    assert Solution().nextPermutation([1, 1, 5]) == [1, 5, 1], Solution().nextPermutation([1, 1, 5])
