#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


"""
使用hashSet纪录所有的数字
然后取一个数字，向左右循环，递增/递减，判断下一个数字是否在set中
每遍历过一个数字，就将它标记为已遍历
"""


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        tmp = set()
        max_length = 0
        for i in nums:
            if i in tmp:
                continue
            tmp.add(i)
            length = 1
            for num in [i - index for index in range(1, len(nums))]:
                if num not in num_set:
                    break
                length += 1
                tmp.add(num)
            for num in [i + index for index in range(1, len(nums))]:
                if num not in num_set:
                    break
                length += 1
                tmp.add(num)
            max_length = max(max_length, length)
        return max_length


if __name__ == '__main__':
    print(Solution().longestConsecutive([0, -1]), 2)
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
