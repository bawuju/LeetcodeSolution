#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        m = prices[0]
        remain = 0
        for price in prices:
            m = min(m, price)
            remain = max(price - m, remain)
        return remain


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
