#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


"""
用递归列出所有可能的组合超时（即使缓存相同长度的排列方式也会超时）
目前找到规律，长度为N的组合数量是长度(N-1)的组合数量的N倍
"""


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return '1'
        indexes = [i + 1 for i in range(n)]
        s = {1: 1}
        for i in range(2, n + 1):
            s[i] = s[i - 1] * i
        tmp = []
        for i in range(n, 0, -1):
            sub_indexes = [index for index in indexes if index not in tmp]
            if i == 1:
                tmp.append(sub_indexes[0])
            else:
                last_s = s[i - 1]
                tmp.append(sub_indexes[k // last_s if k % last_s else k // last_s - 1])
                k = k % last_s
        result = ''
        for index in tmp:
            result += str(index)
        return result


if __name__ == '__main__':
    print(Solution().getPermutation(3, 3), '213')
    print(Solution().getPermutation(4, 9), '2314')
