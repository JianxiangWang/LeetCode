# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        low = 1
        high = n

        while low <= high:
            mid = (low + high) / 2
            if isBadVersion(mid):
                high = mid - 1
                if not isBadVersion(high):
                    return high
            else:
                low = mid + 1
                if isBadVersion(low):
                    return low

