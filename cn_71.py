#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


"""
使用栈
空：不做处理
.：出栈
..：出栈
...：出栈
"""


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for p in path.split('/'):
            if p == '' or p == '.':
                continue
            if p == '..':
                if len(stack) > 0:
                    stack.pop()
                continue
            stack.append(p)
        return ''.join(['/' + p for p in stack]) if stack else '/'


if __name__ == '__main__':
    print(Solution().simplifyPath('/home/'), '/home')
    print(Solution().simplifyPath('/../'), '/')
    print(Solution().simplifyPath('/home//foo/'), '/home/foo')
    print(Solution().simplifyPath('/a/./b/../../c/'), '/c')
    print(Solution().simplifyPath('/a/../../b/../c//.//'), '/c')
    print(Solution().simplifyPath('/a//b////c/d//././/..'), '/a/b/c')
