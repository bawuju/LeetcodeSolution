#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        current = head.next
        last = head
        head.next = None
        while current is not None:
            n = current.next
            current.next = last
            last = current
            current = n
        return last
