#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


# Definition for an interval.
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
        results = []
        sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
        target = None
        for interval in sorted_intervals:
            if target is None:
                target = Interval(interval.start, interval.end)
                continue
            if interval.start > target.end:
                results.append(target)
                target = Interval(interval.start, interval.end)
                continue
            if interval.end > target.end:
                target.end = interval.end
                continue
        if target is not None:
            results.append(target)
        return results


if __name__ == '__main__':
    for i in Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]):
        print(i.start, i.end)
    print('------')
    for i in Solution().merge([Interval(1, 4), Interval(0, 4)]):
        print(i.start, i.end)
    print('------')
    for i in Solution().merge([Interval(1, 4), Interval(0, 1)]):
        print(i.start, i.end)
    print('------')
    for i in Solution().merge([Interval(1, 4), Interval(2, 3)]):
        print(i.start, i.end)
    print('------')
    for i in Solution().merge([Interval(2, 3), Interval(4, 5), Interval(6, 7), Interval(8, 9), Interval(1, 10)]):
        print(i.start, i.end)
