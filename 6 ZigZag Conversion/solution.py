#!/usr/bin/env python
#encoding: utf-8
import sys

import operator

reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def convert(self, s, numRows):

        if numRows < 2 or numRows >= len(s):
            return s

        zigzag = [[] for _ in range(numRows)]
        row, step = 0, 1
        for c in s:
            zigzag[row] += c
            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1
            row += step

        return "".join(map(lambda x: "".join(x), zigzag))






if __name__ == '__main__':
    print Solution().convert("", 1)

