#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r = Solution.inner_subsets(nums, 0, len(nums))
        r.append([])
        return r

    @staticmethod
    def inner_subsets(nums, start, end):
        if end - start == 1:
            return [[nums[start]]]
        sub_result = Solution.inner_subsets(nums, start, end - 1)
        sub_result_cp = []
        for r in sub_result:
            t = r[::]
            t.append(nums[end - 1])
            sub_result_cp.append(t)
        sub_result.extend(sub_result_cp)
        sub_result.append([nums[end - 1]])
        return sub_result


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
