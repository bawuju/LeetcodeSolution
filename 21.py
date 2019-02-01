#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = ListNode(0)
        last = node
        while l1 is not None or l2 is not None:
            current = None
            if l2 is None:
                current = ListNode(l1.val)
                l1 = l1.next
            elif l1 is None:
                current = ListNode(l2.val)
                l2 = l2.next
            elif l1.val > l2.val:
                current = ListNode(l2.val)
                l2 = l2.next
            else:
                current = ListNode(l1.val)
                l1 = l1.next
            last.next = current
            last = current
        return node.next
