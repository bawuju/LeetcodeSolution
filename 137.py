#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0
        two = 0
        for integer in nums:
            one = one ^ integer & ~two
            two = two ^ integer & ~one
        return one


if __name__ == '__main__':
    assert Solution().singleNumber([3, 6, 5, 3, 6, 8, 5, 3, 6, 5]) == 8
