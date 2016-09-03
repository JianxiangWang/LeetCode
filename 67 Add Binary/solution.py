#!/usr/bin/env python
#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a_int = int(a, 2)
        b_int = int(b, 2)

        ans = a_int + b_int

        return bin(ans)[2:]

if __name__ == '__main__':
    print Solution().addBinary("11", "1")