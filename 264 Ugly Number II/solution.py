# encoding: utf-8

# 状态转移
# dp[i] 表示第i个丑数
# dp[i] = dp[: i-1] * 2, dp[: i-1] * 3, dp[: i-1] * 5,  中比dp[i-1]大的最小数
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [None] * n
        dp[0] = 1

        for i in range(1, n):
            L1 = map(lambda x: x*2, dp[:i])
            L2 = map(lambda x: x*3, dp[:i])
            L3 = map(lambda x: x*5, dp[:i])

            dp[i] = min([x for x in L1 + L2 + L3 if x > dp[i-1]])

        return dp[-1]


if __name__ == '__main__':
    print Solution().nthUglyNumber(263)

