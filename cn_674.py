#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


"""
双指针
"""


class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_length = 1
        left = 0
        right = 1
        while right < len(nums):
            if nums[right] > nums[right - 1]:
                right += 1
            else:
                max_length = max(max_length, right - left)
                left = right
                right += 1
        return max(max_length, right - left)


if __name__ == '__main__':
    print(Solution().findLengthOfLCIS([1, 3, 5, 7]), 4)
    print(Solution().findLengthOfLCIS([1, 3, 5, 4, 7]), 3)
    print(Solution().findLengthOfLCIS([2, 2, 2, 2, 2]), 1)
