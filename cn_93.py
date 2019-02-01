#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


"""
暴力解法，直接三层for遍历
要注意的是可能会有两个0连在一起，这里直接用len(sub_address) != len(str(int(sub_address)))简单粗暴解决了
"""


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    if i + j + k >= len(s):
                        continue
                    tmp = [s[:i], s[i:i + j], s[i + j:i + j + k], s[i + j + k:]]
                    error = False
                    for sub_address in tmp:
                        if int(sub_address) > 255 or len(sub_address) != len(str(int(sub_address))):
                            error = True
                            break
                    if not error:
                        address = ''
                        for index in range(len(tmp)):
                            address += str(tmp[index])
                            if index < len(tmp) - 1:
                                address += '.'
                        result.append(address)
        return result


if __name__ == '__main__':
    print(Solution().restoreIpAddresses('010010'), ["0.10.0.10", "0.100.1.0"])
    print(Solution().restoreIpAddresses('25525511135'), ["255.255.11.135", "255.255.111.35"])
