#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n + 1):
            is_three = i % 3 == 0
            is_five = i % 5 == 0
            if is_three and is_five:
                result.append('FizzBuzz')
            elif is_three:
                result.append('Fizz')
            elif is_five:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result


if __name__ == '__main__':
    pass
