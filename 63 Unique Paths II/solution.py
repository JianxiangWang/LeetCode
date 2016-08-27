# encoding: utf-8

# dp
# 与 62 Unique Paths 类似:
# dp[i][j] = dp[i-1][j] + dp[i][j-1], 只是需要判断如果是从障碍物过来的, 为0
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[None] * n for x in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if obstacleGrid[i][j] == 1:
                        return 0
                    else:
                        dp[i][j] = 1
                        continue

                if i - 1 < 0 or obstacleGrid[i-1][j] == 1:
                    a = 0
                else:
                    a = dp[i-1][j]

                if j - 1 < 0 or obstacleGrid[i][j-1] == 1:
                    b = 0
                else:
                    b = dp[i][j-1]

                dp[i][j] = a + b


        # dp 存的是到达 i,j 的路径数量, 对于最后一个, 如果是 障碍物, 则return 0
        if obstacleGrid[-1][-1] == 1:
            return 0

        return dp[-1][-1]


if __name__ == '__main__':

    obstacleGrid = [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]

    print Solution().uniquePathsWithObstacles([[0]])



