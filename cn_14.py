#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        length = 0
        finish = False
        while not finish:
            target_char = None
            for s in strs:
                if length >= len(s) or (target_char is not None and s[length] != target_char):
                    finish = True
                    break
                target_char = s[length]
            if not finish:
                length += 1
        return strs[0][0:length]


if __name__ == '__main__':
    print(Solution().longestCommonPrefix([]), '')
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]), 'fl')
    print(Solution().longestCommonPrefix(["dog", "racecar", "car"]), '')
