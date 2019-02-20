#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        len2 = len(num2)
        base = ord('0')
        index = 0
        last_sum = 0
        cache = []
        while True:
            if index >= len1 and index >= len2 and last_sum == 0:
                break
            s1 = ord(num1[len1 - index - 1] if index < len1 else '0') - base
            s2 = ord(num2[len2 - index - 1] if index < len2 else '0') - base
            s = s1 + s2 + last_sum
            cache.append(chr(s % 10 + base))
            last_sum = s // 10
            index += 1
        # join的效率比用加号更高
        return ''.join(cache[::-1])


if __name__ == '__main__':
    assert Solution().addStrings('0', '0') == '0'
    assert Solution().addStrings('45648', '18743') == '64391'
    assert Solution().addStrings('450648', '18743') == '469391'
