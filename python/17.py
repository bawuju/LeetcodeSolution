#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits:
            return []
        result = ['']
        for index in range(len(digits)):
            result = [last + current for last in result for current in mapping[digits[index]]]
        return result


if __name__ == '__main__':
    assert Solution().letterCombinations('2') == ['a', 'b', 'c']
    assert Solution().letterCombinations('') == []
    assert Solution().letterCombinations('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
