# encoding: utf-8

# dp[i] = dp[i-1] + dp[i-2]: 跨到第i台阶 == 从i-1跨过来的次数 + 从i-2跨过来的次数
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return 1

        dp = [None] * n
        dp[0] = 1
        dp[1] = 2

        for idx in range(2, n):
            dp[idx] = dp[idx - 1] + dp[idx - 2]
        return dp[n-1]



if __name__ == '__main__':
    print Solution().climbStairs(3)