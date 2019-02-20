#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


"""
基于快速排序-三向切分改造而来的快速选择算法
"""


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return Solution.quick_select(nums, 0, len(nums) - 1, len(nums) - k)

    @staticmethod
    def quick_select(nums, start, end, k):
        if start >= end:
            return nums[k]
        pivot = nums[start]
        '''
        三个指针
        point1代表这个指针之前的比pivot小
        point2代表这个指针与point1之间的跟pivot相等
        point3代表这个指针之后的比pivot大
        '''
        point1, point2, point3 = start, start + 1, end
        while point2 <= point3:
            if nums[point2] < pivot:
                nums[point1], nums[point2] = nums[point2], nums[point1]
                point1 += 1
                point2 += 1
            elif nums[point2] == pivot:
                point2 += 1
            else:
                nums[point2], nums[point3] = nums[point3], nums[point2]
                point3 -= 1
        if k < point1:
            return Solution.quick_select(nums, start, point1 - 1, k)
        elif k > point2 - 1:
            return Solution.quick_select(nums, point2, end, k)
        else:
            return nums[k]


if __name__ == '__main__':
    print(Solution().findKthLargest([2, 1], 1), 2)
    print(Solution().findKthLargest([1], 1), 1)
    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
    print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
