#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution(object):

    # 比较慢的方法
    def smallestDistancePair_1(self, nums, k):
        nums.sort()

        # multiplicity
        multiplicity = [0] * len(nums)
        for index in range(1, len(nums)):
            if nums[index - 1] == nums[index]:
                multiplicity[index] = multiplicity[index - 1] + 1

        # prefix
        prefix = [0] * (nums[-1]) * 2
        index_of_lesser = 0
        for index in range(len(prefix)):
            while index_of_lesser < len(nums) and nums[index_of_lesser] == index:
                index_of_lesser += 1
            prefix[index] = index_of_lesser

        def possible(guess):
            count = 0
            for i in range(len(nums)):
                count += prefix[nums[i] + guess] - prefix[nums[i]] + multiplicity[i]
            return count >= k

        mi = 0
        ma = nums[-1] - nums[0]
        while mi < ma:
            mid = (mi + ma) // 2
            if possible(mid):
                ma = mid
            else:
                mi = mid + 1
        return mi

    # 比较快的方法
    def smallestDistancePair_2(self, nums, k):
        nums.sort()

        def possible(guess):
            count = 0
            left = 0
            for right, num in enumerate(nums):
                while num - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        mi = 0
        ma = nums[-1] - nums[0]
        while mi < ma:
            mid = (mi + ma) // 2
            if possible(mid):
                ma = mid
            else:
                mi = mid + 1
        return mi


if __name__ == '__main__':
    assert Solution().smallestDistancePair_1([1, 3, 1], 1) == 0
    assert Solution().smallestDistancePair_2([1, 3, 1], 1) == 0
