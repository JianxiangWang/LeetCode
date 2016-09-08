#!/usr/bin/env python
#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        ans = ''
        while n:
            ans = chr(ord('A') + (n - 1) % 26) + ans
            n = (n - 1) / 26
        return ans


if __name__ == '__main__':

    print Solution().convertToTitle(701)