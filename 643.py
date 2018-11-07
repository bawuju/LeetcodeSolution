#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        difference = 0
        index_start = 0
        for offset in range(len(nums) - k):
            difference += (nums[offset + k] - nums[offset])
            if difference > 0:
                index_start = offset + 1
                difference = 0

        sum_loop = 0
        for index in range(index_start, index_start + k):
            sum_loop += nums[index]
        average = sum_loop / k
        return average
        

if __name__ == '__main__':
    assert Solution().findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75
