#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def custom_assert(node, result):
    for r in result:
        assert node.val == r
        node = node.next
    assert node is None


def build_node(value_list):
    node_list = [ListNode(value) for value in value_list]
    for index in range(len(node_list) - 1):
        node_list[index].next = node_list[index + 1]
    return node_list[0]


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmp = []
        while head is not None:
            tmp.append(head)
            head = head.next
        if len(tmp) == 1 and n == 1:
            return None
        if n == 1:
            tmp[-2].next = None
            return tmp[0]
        index = len(tmp) - n - 1
        if index < 0:
            return tmp[1]
        tmp[index].next = tmp[index + 2]
        return tmp[0]


if __name__ == '__main__':
    custom_assert(Solution().removeNthFromEnd(build_node([1, 2, 3, 4, 5]), 2), [1, 2, 3, 5])
    custom_assert(Solution().removeNthFromEnd(build_node([1]), 1), [])
    custom_assert(Solution().removeNthFromEnd(build_node([1, 2]), 2), [2])
    custom_assert(Solution().removeNthFromEnd(build_node([1, 2]), 1), [1])
