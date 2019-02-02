#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = Solution.get_num(l1) + Solution.get_num(l2)
        if s == 0:
            return ListNode(0)
        else:
            result = None
            last = None
            while s != 0:
                tmp = ListNode(s % 10)
                s = s // 10
                if result is None:
                    result = tmp
                    last = tmp
                else:
                    last.next = tmp
                    last = tmp
            return result

    @staticmethod
    def get_num(l):
        if l.val == 0 and l.next is None:
            return 0
        else:
            tmp = 0
            index = 0
            while l is not None:
                tmp += l.val * pow(10, index)
                index += 1
                l = l.next
            return tmp
