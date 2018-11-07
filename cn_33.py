#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


"""
先找旋转轴
然后二分查找
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        axis = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                axis = i
                break
        result = Solution.bin_search(nums[:axis], target)
        if result >= 0:
            return result
        result = Solution.bin_search(nums[axis:], target)
        if result >= 0:
            return result + axis
        return -1

    @staticmethod
    def bin_search(nums, target):
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
        return -1


if __name__ == '__main__':
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0), 4)
