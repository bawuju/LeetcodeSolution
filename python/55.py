#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        index = 0
        length = len(nums)
        while index <= reach and index < length:
            reach = max(reach, index + nums[index])
            index += 1
        return index == length


if __name__ == '__main__':
    assert Solution().canJump([2, 3, 1, 1, 4])
    assert not Solution().canJump([3, 2, 1, 0, 4])
    assert Solution().canJump([2, 0])
