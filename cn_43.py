#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        if len(num1) == 1 and len(num2) == 1:
            n1 = ord(num1) - ord('0')
            n2 = ord(num2) - ord('0')
            result = []
            num = n1 * n2
            while num > 0:
                result.insert(0, chr(num % 10 + ord('0')))
                num = num // 10
            return ''.join(result)
        if len(num2) > 1:
            num1, num2 = num2, num1
        if len(num1) > 1:
            result_list = []
            for c_index in range(len(num1)):
                result_list.append(self.multiply(num1[c_index], num2) + '0' * (len(num1) - c_index - 1))
            result = []
            tmp = 0
            next_tmp = 0
            for i in range(max([len(s) for s in result_list])):
                for r in result_list:
                    if i >= len(r):
                        continue
                    tmp += ord(r[len(r) - i - 1]) - ord('0')
                tmp += next_tmp
                result.insert(0, chr(tmp % 10 + ord('0')))
                next_tmp = tmp // 10
                tmp = 0
            while next_tmp > 0:
                result.insert(0, chr(next_tmp % 10 + ord('0')))
                next_tmp = next_tmp // 10
            return ''.join(result)


if __name__ == '__main__':
    print(Solution().multiply('2', '3'), '6')
    print(Solution().multiply('123', '456'), '56088')
