#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        index = 0
        length = len(s)
        for c in t:
            if s[index] == c:
                index += 1
                if index == length:
                    return True
        return False

if __name__ == '__main__':
    assert Solution().isSubsequence('abc', 'ahbgdc')
    assert not Solution().isSubsequence('axc', 'ahbgdc')
