#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        v = 0
        i = 0
        while i < len(height):
            # 如果下一个数字比当前的大，直接挑过
            if i < len(height) - 1 and height[i] <= height[i + 1]:
                i += 1
                continue
            # 开始向右遍历
            # 如果寻找到比当前位置的大的，就直接返回
            # 否则就纪录遍历过程中最大的那个值的位置，直到遍历结束
            start = i
            end = i + 1
            max_size = 0
            max_size_index = 0
            while end < len(height):
                if height[end] > height[start]:
                    max_size = height[end]
                    max_size_index = end
                    break
                else:
                    if height[end] > max_size:
                        max_size = height[end]
                        max_size_index = end
                    end += 1
            # 没有找到更大的，返回
            if max_size == 0:
                break
            end = max_size_index
            used = sum(height[start + 1:end])
            v += min(height[start], height[end]) * (end - start - 1) - used
            i = end
        return v


if __name__ == '__main__':
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
    print(Solution().trap([0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]), 0)
