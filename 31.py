#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        先找到最后一个升序，提取这个升序后面的降序(因为是最后一个升序，所以它之后必定都是降序)的"比升序大的最小值"
        与升序最后一个数字调换。调换之后，后面的数字按升序排列
        """
        # 最后一个升序结束的index
        target_index = -1
        for index in range(len(nums) - 1, 0, -1):
            if nums[index] > nums[index - 1]:
                target_index = index
                break
        if target_index == -1:
            Solution.swap(nums, 0, len(nums))
        else:
            # 需要被拉到前面的index
            change_index_left = target_index - 1
            change_index_right = target_index
            for index in range(change_index_right, len(nums)):
                if nums[change_index_left] < nums[index] <= nums[change_index_right]:
                    change_index_right = index
            nums[change_index_left], nums[change_index_right] = nums[change_index_right], nums[change_index_left]
            # 后面的降序排序为升序
            Solution.swap(nums, target_index, len(nums))
        return nums

    @staticmethod
    def swap(nums, start, end):
        for index in range(start, end):
            left = index
            right = end - 1 - (index - start)
            if left >= right:
                break
            nums[left], nums[right] = nums[right], nums[left]


if __name__ == '__main__':
    assert Solution().nextPermutation([2, 3, 1, 3, 3]) == [2, 3, 3, 1, 3], Solution().nextPermutation([2, 3, 1, 3, 3])
    assert Solution().nextPermutation([6, 8, 2, 1, 3, 4, 7, 5]) == [6, 8, 2, 1, 3, 5, 4, 7], Solution().nextPermutation(
        [6, 8, 2, 1, 3, 4, 7, 5])
    assert Solution().nextPermutation([1, 2, 3]) == [1, 3, 2], Solution().nextPermutation([1, 2, 3])
    assert Solution().nextPermutation([3, 2, 1]) == [1, 2, 3], Solution().nextPermutation([3, 2, 1])
    assert Solution().nextPermutation([1, 1, 5]) == [1, 5, 1], Solution().nextPermutation([1, 1, 5])
