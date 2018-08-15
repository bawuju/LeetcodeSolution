#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for sub_str in strs:
            sorted_str = ''.join(sorted(sub_str))
            if sorted_str not in result.keys():
                result[sorted_str] = []
            result[sorted_str].append(sub_str)
        return list(result.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
