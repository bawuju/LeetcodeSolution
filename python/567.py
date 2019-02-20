#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        target_hash = sum([hash(s) for s in s1])
        tmp_hash = sum([hash(s) for s in s2[0:len(s1)]])
        if target_hash == tmp_hash:
            return True
        left = 0
        right = len(s1)
        while right < len(s2):
            tmp_hash = tmp_hash - hash(s2[left]) + hash(s2[right])
            if tmp_hash == target_hash:
                return True
            left += 1
            right += 1
        return False


if __name__ == '__main__':
    print(Solution().checkInclusion('adc', 'dcda'), True)
    print(Solution().checkInclusion('ab', 'eidbaooo'), True)
    print(Solution().checkInclusion('ab', 'eidboaoo'), False)
