# encoding: utf-8

# 从上往下,从左往右遍历
# dp[i,j] = min(dp[i-1, j] + grid[i, j], dp[i, j-1] + grid[i, j] )
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def min_one(a, b):
            if a == None and b == None:
                return 0
            if a == None:
                return b
            if b == None:
                return a
            return min(a, b)

        n = len(grid)
        m = len(grid[0])

        dp = [[None] * m for x in range(n)]

        for i in range(n):
            for j in range(m):
                if i - 1 < 0:
                    a = None
                else:
                    a = dp[i-1][j]

                if j - 1 < 0:
                    b = None
                else:
                    b = dp[i][j-1]

                dp[i][j] = min_one(a, b) + grid[i][j]

        return dp[-1][-1]


if __name__ == '__main__':

    grid = [
        [1, 4, 2],
        [1, 4, 2],
        [1, 1, 1],
    ]
    print Solution().minPathSum(grid)
