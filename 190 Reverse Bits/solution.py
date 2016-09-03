#!/usr/bin/env python
#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = bin(n)

        # 不到32位,变成32位
        if len(b) < 34:
            b = '0b' + '0' * (34 - len(b)) + b[2:]

        reversed_b = "0b" + b[2:][::-1]

        return int(reversed_b, 2)

if __name__ == '__main__':

    print Solution().reverseBits(43261596)


