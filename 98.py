#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return Solution.is_valid_BST(root, None, None)

    @staticmethod
    def check_range(target, min_val, max_val):
        return (min_val if min_val is not None else target.val - 1) < target.val < (
            max_val if max_val is not None else target.val + 1)

    @staticmethod
    def is_valid_BST(target, min_val, max_val):
        left = target.left
        right = target.right
        if left is not None and right is not None:
            return Solution.check_range(target, min_val, max_val) \
                   and Solution.is_valid_BST(left, min_val, target.val if not max_val else min(max_val, target.val)) \
                   and Solution.is_valid_BST(right, target.val if not min_val else max(min_val, target.val), max_val)
        if left is not None:
            return Solution.check_range(target, min_val, max_val) \
                   and Solution.is_valid_BST(left, min_val, target.val if not max_val else min(max_val, target.val))
        if right is not None:
            return Solution.check_range(target, min_val, max_val) \
                   and Solution.is_valid_BST(right, target.val if not min_val else max(min_val, target.val), max_val)
        return Solution.check_range(target, min_val, max_val)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(6)
    assert Solution().isValidBST(root)

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(20)
    assert not Solution().isValidBST(root)

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    assert not Solution().isValidBST(root)

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert Solution().isValidBST(root)
