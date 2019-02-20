#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index_0 = 0
        index_1 = 0
        index_2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[index_2] = 2
                index_2 += 1
                nums[index_1] = 1
                index_1 += 1
                nums[index_0] = 0
                index_0 += 1
                continue
            if nums[i] == 1:
                nums[index_2] = 2
                index_2 += 1
                nums[index_1] = 1
                index_1 += 1
                continue
            if nums[i] == 2:
                nums[index_2] = 2
                index_2 += 1
                continue
        return nums


if __name__ == '__main__':
    print(Solution().sortColors([2, 0, 2, 1, 1, 0]))
