#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
三向切分的快排
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '%d' % self.val


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        Solution.sort(head, None)
        return head

    @staticmethod
    def swap(l1, l2):
        l1.val, l2.val = l2.val, l1.val

    @staticmethod
    def sort(left, right):
        if left == right:
            return
        pivot = left.val
        current = left.next
        point1, point1_last, point2 = left.next, left, left.next
        while current != right:
            if current.val < pivot:
                Solution.swap(current, point1)
                if point1 != point2:
                    Solution.swap(current, point2)
                current = current.next
                point1_last = point1
                point1 = point1.next
                point2 = point2.next
            elif current.val > pivot:
                current = current.next
            else:
                Solution.swap(current, point2)
                current = current.next
                point2 = point2.next
        Solution.swap(point1_last, left)
        Solution.sort(left, point1_last)
        Solution.sort(point2, right)


def num_to_node(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    last = head
    for i in range(1, len(nums)):
        tmp = ListNode(nums[i])
        last.next = tmp
        last = tmp
    return head


def node_to_num(node):
    if node is None:
        return []
    nums = []
    while node is not None:
        nums.append(node.val)
        node = node.next
    return nums


if __name__ == '__main__':
    print(node_to_num(Solution().sortList(num_to_node([1, 3, 3, 2]))))
    print(node_to_num(Solution().sortList(num_to_node([4, 2, 1, 3]))))
    print(node_to_num(Solution().sortList(num_to_node([-1, 5, 3, 4, 0]))))
    print(node_to_num(Solution().sortList(num_to_node(
        [-84, 142, 41, -17, -71, 170, 186, 183, -21, -76, 76, 10, 29, 81, 112, -39, -6, -43, 58, 41, 111, 33, 69, 97,
         -38, 82, -44, -7, 99, 135, 42, 150, 149, -21, -30, 164, 153, 92, 180, -61, 99, -81, 147, 109, 34, 98, 14, 178,
         105, 5, 43, 46, 40, -37, 23, 16, 123, -53, 34, 192, -73, 94, 39, 96, 115, 88, -31, -96, 106, 131, 64, 189, -91,
         -34, -56, -22, 105, 104, 22, -31, -43, 90, 96, 65, -85, 184, 85, 90, 118, 152, -31, 161, 22, 104, -85, 160,
         120, -31, 144, 115]))))
