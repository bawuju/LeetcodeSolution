#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return mid + 1 if nums[mid] < target else mid


if __name__ == '__main__':
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2, Solution().searchInsert([1, 3, 5, 6], 5)
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1, Solution().searchInsert([1, 3, 5, 6], 2)
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4, Solution().searchInsert([1, 3, 5, 6], 7)
    assert Solution().searchInsert([1, 3, 5, 6], 0) == 0, Solution().searchInsert([1, 3, 5, 6], 0)
