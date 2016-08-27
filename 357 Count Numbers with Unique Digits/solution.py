
#
# dp[1] = 0
# dp[2] = 9
# dp[i] = dp[i-1] * 10 (i>=2)
# dp[i] 表示应该排除的
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
