#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        Solution.backtrack(result, [], 0, candidates, 0, target)
        return result

    @staticmethod
    def backtrack(result, tmp, start, nums, s, target):
        if s > target:
            return
        elif s == target:
            result.append(tmp[::])
        else:
            for index in range(start, len(nums)):
                num = nums[index]
                tmp.append(num)
                Solution.backtrack(result, tmp, index, nums, s + num, target)
                tmp.pop()


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
    print(Solution().combinationSum([2, 3, 5], 8))
