#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sorted(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False
        half = s // 2
        sum_list = [False] * (half + 1)
        for num in nums:
            if num > half:
                break
            for index in range(half, 0, -1):
                if index - num < 0:
                    break
                sum_list[index] |= sum_list[index - num]
            sum_list[num] = True
            if sum_list[half]:
                return True
        return sum_list[half]


if __name__ == '__main__':
    assert Solution().canPartition([1, 5, 11, 5]) is True
    assert Solution().canPartition([1, 2, 5]) is False
    assert Solution().canPartition([2, 2, 3, 5]) is False
    assert Solution().canPartition(
        [19, 33, 38, 60, 81, 49, 13, 61, 50, 73, 60, 82, 73, 29, 65, 62, 53, 29, 53, 86, 16, 83, 52, 67, 41, 53, 18, 48,
         32, 35, 51, 72, 22, 22, 76, 97, 68, 88, 64, 19, 76, 66, 45, 29, 95, 24, 95, 29, 95, 76, 65, 35, 24, 85, 95, 87,
         64, 97, 75, 88, 88, 65, 43, 79, 6, 5, 70, 51, 73, 87, 76, 68, 56, 57, 69, 77, 22, 27, 29, 12, 55, 58, 18, 30,
         66, 53, 53, 81, 94, 76, 28, 41, 77, 17, 60, 32, 62, 62, 88, 61]) is True
