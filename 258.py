#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            num = Solution.run(num)
        return num

    @staticmethod
    def run(num):
        sum_digits = 0
        while num > 0:
            sum_digits += num % 10
            num //= 10
        return sum_digits
        

if __name__ == '__main__':
    assert Solution().addDigits(38) == 2
