#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index_map = {}
        right = 0
        max_length = 0
        current_length = 0
        while right < len(s):
            if s[right] not in index_map.keys():
                current_length += 1
            else:
                left = index_map[s[right]] + 1
                index_map = {key: value for key, value in index_map.items() if value >= left}
                max_length = max(max_length, current_length)
                current_length = right - left + 1
            index_map[s[right]] = right
            right += 1
        return max(max_length, current_length)


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('aab'), 2)
    print(Solution().lengthOfLongestSubstring('abcabcbb'), 3)
    print(Solution().lengthOfLongestSubstring('bbbbb'), 1)
    print(Solution().lengthOfLongestSubstring('pwwkew'), 3)
