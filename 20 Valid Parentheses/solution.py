#!/usr/bin/env python
#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for c in s:
            if c in "({[":
                stack.append(c)
            elif c in ")}]":

                if len(stack) == 0:
                    return False
                if c == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False

                if c == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False

                if c == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False

        if stack == []:
            return True
        else:
            return False

if __name__ == '__main__':
    print Solution().isValid("]")

