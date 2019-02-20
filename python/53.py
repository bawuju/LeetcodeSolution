#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum, target_sum = nums[0], 0
        for num in nums:
            target_sum += num
            max_sum = max(max_sum, target_sum)
            target_sum = max(0, target_sum)
        return max_sum


if __name__ == '__main__':
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
