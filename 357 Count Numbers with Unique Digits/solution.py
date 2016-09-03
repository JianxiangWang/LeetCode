# encoding: utf-8

#
# dp[1] = 10
# dp[2] = 91 = 10 + 9*9
# dp[i] = dp[i-1] + 9*9*8*7..*(9-k+2) (共i个)
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 1

        dp = [None] * (n + 1)
        dp[1] = 10

        for i in range(2, n+1):

            t = 9
            for j in range(i-1):
                t *= (9-j)

            dp[i] = dp[i-1] + t

        return dp[-1]

    # try Backtracking
    def countNumbersWithUniqueDigits2(self, n):
        pass


if __name__ == '__main__':
    print Solution().countNumbersWithUniqueDigits(3)
