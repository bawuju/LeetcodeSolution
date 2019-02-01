#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
三数之和可以转换成1个数字+两数之和
两数之和用双指针逐步靠近
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = {}
        for i in range(len(nums) - 2):
            point = Solution.search(nums, -nums[i], i + 1)
            if not point:
                continue
            for p in point:
                result[(nums[i], nums[p[0]], nums[p[1]])] = 'TAG'
        return [list(i) for i in list(result.keys())]

    @staticmethod
    def search(nums, target, left):
        result = []
        right = len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                result.append([left, right])
                left += 1
            elif s < target:
                left += 1
            else:
                right -= 1
        return result


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])
    print(Solution().threeSum([-2, 0, 1, 1, 2]), [[-2, 0, 2], [-2, 1, 1]])
