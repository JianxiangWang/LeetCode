# encoding: utf-8

# 因为最多可以进行两次交易, 且 you must sell the stock before you buy again
# 所以, 可以首先将数组划分成两部分, 分别在这两部分中求最大, 他们的和就是当前划分的最大利润
# 穷举所有可能,就可以得到最大利润

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1:
            return 0

        # dp1[i] 表示从 0-i, 包含i的最大利润
        dp1 = [None] * len(prices)
        dp1[0] = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            dp1[i] = max(dp1[i-1], prices[i] - min_price)
            min_price = min(min_price, prices[i])

        # dp2[i] 表示 i 到 N 的最大利润
        # 反向遍历, dp[i] = max(dp[i+1], prices[i] - max_price)
        dp2 = [None] * len(prices)
        dp2[-1] = 0
        max_price = prices[-1]
        for i in range(0, len(prices)-1)[::-1]:
            dp2[i] = max(dp2[i+1], max_price - prices[i])
            max_price = max(prices[i], max_price)

        # 有了dp1, dp2, 遍历所有的划分, 获取最大profit
        max_profit = 0
        for i in range(len(prices)):
            profit_1 = dp1[i]
            if i + 1 > len(prices) - 1:
                profit_2 = 0
            else:
                profit_2 = dp2[i + 1]

            if profit_1 + profit_2 > max_profit:
                max_profit = profit_1 + profit_2

        return max_profit


if __name__ == '__main__':
    print Solution().maxProfit([2, 4, 6, 1, 3, 8, 3])




