#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    assert Solution().search([3, 1], 1) == 1
    assert Solution().search([1, 3, 5], 5) == 2
    assert Solution().search([1, 3], 3) == 1
    assert Solution().search([1, 3], 1) == 0
    assert Solution().search([1, 3, 5], 1) == 0
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 1) == 5
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 3) == -1
