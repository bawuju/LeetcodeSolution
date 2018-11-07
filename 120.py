#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        distance = [[triangle[0][0]]]
        for i in range(1, len(triangle)):
            current_t = triangle[i]
            current_d = []
            last_d = distance[i - 1]
            for j in range(len(current_t)):
                parent = 0
                if j == 0:
                    parent = last_d[0]
                elif j == len(current_t) - 1:
                    parent = last_d[-1]
                else:
                    parent = min(last_d[j - 1], last_d[j])
                current_d.append(current_t[j] + parent)
            distance.append(current_d)
        return min(distance[-1])