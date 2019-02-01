#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import random
import multiprocessing

"""
快速排序例子（三向切分）
"""


def quick_sort(nums, start, end):
    if start >= end:
        return
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
    quick_sort(nums, start, point1 - 1)
    quick_sort(nums, point2, end)


def test(length):
    tmp = [random.randint(0, 100) for i in range(length)]
    result = tmp[::]
    quick_sort(result, 0, len(result) - 1)
    if sorted(tmp) != result:
        print('测试错误')


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    for i in range(100):
        for l in range(1, 1000):
            pool.apply_async(test, args=(l,))
    pool.close()
    pool.join()
