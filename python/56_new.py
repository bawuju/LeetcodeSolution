#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


"""
先对所有区间按照start进行排序
然后遍历
"""


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda i: i.start)
        tmp = []
        for i in intervals:
            if not tmp:
                tmp.append(i)
                continue
            if tmp[-1].end < i.start:
                tmp.append(i)
                continue
            if i.start <= tmp[-1].end < i.end:
                tmp[-1].end = i.end
        return tmp


def make_interval(data):
    return [Interval(d[0], d[1]) for d in data]


if __name__ == '__main__':
    print(Solution().merge(make_interval([[1, 3], [2, 6], [8, 10], [15, 18]])), [[1, 6], [8, 10], [15, 18]])
    print(Solution().merge(make_interval([[1, 4], [4, 5]])), [[1, 5]])
