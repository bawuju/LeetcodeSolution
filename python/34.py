#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        index_left = -1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                index_left = mid
                break
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        if index_left == -1:
            return [-1, -1]
        index_right = index_left
        while index_left >= 0 and nums[index_left] == target:
            index_left -= 1
        while index_right < len(nums) and nums[index_right] == target:
            index_right += 1
        return [index_left + 1, index_right - 1]


if __name__ == '__main__':
    assert Solution().searchRange([1], 1) == [0, 0]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
