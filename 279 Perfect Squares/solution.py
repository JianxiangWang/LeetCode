#encoding: utf-8

# 动态规划, 可以把他看做一个爬山问题
# dp[i] = min(dp[i-x] for x in [..Squares...]) + 1
class Solution(object):

    # 超时了!!!!
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 0:
            return 0

        dp = [None] * (n + 1)
        dp[0] = 0
        squares = [1]
        x = 1
        for i in range(1, n+1):
            if i >= (x+1)**2:
                x += 1
                squares.append(x**2)

            dp[i] = min([dp[i-square] for square in squares]) + 1

        return dp[-1]



if __name__ == '__main__':
   print  Solution().numSquares(9542)