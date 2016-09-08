#!/usr/bin/env python
#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        i, j = 0, 0

        while j < n:

            while i < m and nums1[i] <= nums2[j]:
                i += 1

            k = m
            while k >i:
                nums1[k] = nums1[k-1]
                k -= 1

            nums1[i] = nums2[j]
            m += 1
            j += 1

if __name__ == '__main__':
    nums1 = [2, 4, 7, None, None, None]
    Solution().merge(nums1, 3, [3, 5, 10], 3)

    print nums1





