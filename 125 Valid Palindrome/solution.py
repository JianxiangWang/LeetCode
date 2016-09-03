#!/usr/bin/env python
#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# two point
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s == "":
            return True

        s = s.lower()
        i = 0
        j = len(s) - 1

        while i < len(s):
            if self.is_alphanumeric(s[i]):
                break
            i += 1

        while j >= 0:
            if self.is_alphanumeric(s[j]):
                break
            j -= 1

        while i <= j:
            if s[i] != s[j]:
                return False

            i += 1
            while i < len(s):
                if self.is_alphanumeric(s[i]):
                    break
                i += 1
            j -= 1
            while j >= 0:
                if self.is_alphanumeric(s[j]):
                    break
                j -= 1

        return True


    def is_alphanumeric(self, c):
        if ord(c) in range(48, 58):
            return True
        if ord(c) in range(97, 123):
            return True
        return False


if __name__ == '__main__':

    print Solution().isPalindrome("race a car")