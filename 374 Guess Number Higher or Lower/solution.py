# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    pass

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        low = 1
        high = n

        while low <= high:
            mid = (low + high) / 2
            x = guess(mid)
            if x == -1:
                high = mid - 1
            if x == 1:
                low = mid + 1
            if x == 0:
                return mid


