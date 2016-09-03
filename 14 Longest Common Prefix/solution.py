#!/usr/bin/env python
#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if strs == []:
            return ""

        min_length = min(map(len, strs))

        ans = []
        for i in range(min_length):
            if len(set([str[i] for str in strs])) == 1:
                ans.append(strs[0][i])
            else:
                break
        return "".join(ans)

if __name__ == '__main__':
    print Solution().longestCommonPrefix(["abc", "a", "a"])
