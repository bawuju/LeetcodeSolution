#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [[nums[0]]]
        elif len(nums) == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        else:
            result = []
            for start in nums:
                sub_range_list = nums[::]
                sub_range_list.remove(start)
                sub_result = []
                for sub in self.permute(sub_range_list):
                    sub.insert(0, start)
                    sub_result.append(sub)
                result.extend(sub_result)
            return result


if __name__ == '__main__':
    print(Solution().permute([1]))
    print(Solution().permute([1, 2, 3]))
