# encoding: utf-8

# 状态转移
# dp[i]表示到i位置, 所取得的最大利润
# dp[i] = dp[i-1], dp[i] - 1..i-1 最小者
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0

        dp = [None] * len(prices)
        dp[0] = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], prices[i] - min_price)

            if prices[i] < min_price:
                min_price = prices[i]

        return dp[-1]


if __name__ == '__main__':
    # print Solution().maxProfit([7, 1, 5, 3, 6, 4])
    print Solution().maxProfit([7, 6, 4, 3, 1])

