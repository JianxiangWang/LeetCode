#!/usr/bin/env python
#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        v1_list = map(int, version1.split("."))
        v2_list = map(int, version2.split("."))


        max_length = max(len(v1_list), len(v2_list))

        if len(v1_list) < max_length:
            v1_list = v1_list + [0] * (max_length - len(v1_list))
        else:
            v2_list = v2_list + [0] * (max_length - len(v2_list))


        for i in range(max_length):
            if v1_list[i] < v2_list[i]:
                return -1
            if v1_list[i] > v2_list[i]:
                return 1

        if len(v1_list) == len(v2_list):
            return 0
        else:
            if len(v1_list) > len(v2_list):
                return 1
            else:
                return -1


if __name__ == '__main__':
    print Solution().compareVersion("1.0", "1")


