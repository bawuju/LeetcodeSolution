#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for m in range(len(board)):
            for n in range(len(board[m])):
                if board[m][n] != word[0]:
                    continue
                if Solution.inner_search(board, word, 0, m, n, [[False] * len(board[0]) for i in range(len(board))]):
                    return True
        return False

    @staticmethod
    def inner_search(board, word, index, m, n, trace):
        # out of range
        if m < 0 or m >= len(board):
            return False
        if n < 0 or n >= len(board[0]):
            return False
        # check trace
        if trace[m][n]:
            return False
        # check charset
        if board[m][n] != word[index]:
            return False
        # check end
        if index == len(word) - 1:
            return True
        # next step
        trace[m][n] = True
        if Solution.inner_search(board, word, index + 1, m + 1, n, trace) \
                or Solution.inner_search(board, word, index + 1, m - 1, n, trace) \
                or Solution.inner_search(board, word, index + 1, m, n + 1, trace) \
                or Solution.inner_search(board, word, index + 1, m, n - 1, trace):
            return True
        trace[m][n] = False
        return False


if __name__ == '__main__':
    test_board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    assert Solution().exist(test_board, 'ABCCED')
    assert Solution().exist(test_board, 'SEE')
    assert not Solution().exist(test_board, 'ABCB')
    assert Solution().exist([['a', 'b'], ['c', 'd']], 'cdba')

# EXAMPLE
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
