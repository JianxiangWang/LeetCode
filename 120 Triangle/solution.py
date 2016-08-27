#encoding: utf-8

# 状态转移
# dp[i, j] 表示从 top 到 i,j 节点的 最小路径和
# dp[i][j] = min(dp[i-1]][j], dp[i-1][j-1]) + triangle[i][j]
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [ [None] * n for x in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):

                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]


        return min(dp[-1])

if __name__ == '__main__':
    s = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    Solution().minimumTotal(s)
