#encoding: utf-8

# dp
# 从上往下,从左往右
# dp[i][j] = dp[i-1][j] + d[i][j-1]
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[None] * n for x in range(m)]

        for i in range(m):
            for j in range(n):
                if i - 1 < 0:
                    a = 0
                else:
                    a = dp[i-1][j]

                if j - 1 < 0:
                    b = 0
                else:
                    b = dp[i][j-1]

                if a == 0 and b==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = a + b


        return dp[m-1][n-1]


if __name__ == '__main__':
    print Solution().uniquePaths(2, 2)


