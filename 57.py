#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __str__(self):
        return '(start: %s; end: %s)' % (self.start, self.end)

    def __repr__(self):
        return self.__str__()


class Solution:
    def insert(self, intervals, new_interval):
        """
        :type intervals: List[Interval]
        :type new_interval: Interval
        :rtype: List[Interval]
        """
        start = new_interval.start
        end = new_interval.end
        left = [i for i in intervals if i.end < start]
        right = [i for i in intervals if i.start > end]
        if len(left) + len(right) != len(intervals):
            start = min(start, intervals[len(left)].start)
            end = max(end, intervals[-len(right) - 1].end)
        return left + [Interval(start, end)] + right


def test(interval_list, interval_insert, result):
    interval_obj_list = []
    for interval in interval_list:
        interval_obj_list.append(Interval(interval[0], interval[1]))
    interval_result_list = []
    for interval in result:
        interval_result_list.append(Interval(interval[0], interval[1]))
    assert Solution().insert(interval_obj_list,
                             Interval(interval_insert[0], interval_insert[1])) == interval_result_list


if __name__ == '__main__':
    test([[1, 5]], [0, 3], [[0, 5]])
    test([[4, 5], [6, 9]], [2, 3], [[2, 3], [4, 5], [6, 9]])
    test([[1, 3], [6, 9]], [10, 11], [[1, 3], [6, 9], [10, 11]])
    test([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]])
    test([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 9], [[1, 2], [3, 10], [12, 16]])
    print('success')
