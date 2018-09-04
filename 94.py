#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        r = []
        tmp = [root]
        trace = set()
        while tmp:
            target = tmp[-1]
            next_left = target.left
            next_right = target.right
            # left
            if next_left and next_left not in trace:
                tmp.append(next_left)
                continue
            # inorder
            r.append(target.val)
            trace.add(target)
            tmp.pop()
            # right
            if next_right and next_right not in trace:
                tmp.append(next_right)
                continue
        return r


class Solution2:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        r = []
        tmp = []
        target = root
        while tmp or target:
            while target:
                tmp.append(target)
                target = target.left
            target = tmp.pop()
            r.append(target.val)
            target = target.right
        return r


if __name__ == '__main__':
    test_tree = TreeNode(1)
    test_tree.right = TreeNode(2)
    test_tree.right.left = TreeNode(3)
    assert Solution1().inorderTraversal(test_tree) == [1, 3, 2]

# Input:
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
