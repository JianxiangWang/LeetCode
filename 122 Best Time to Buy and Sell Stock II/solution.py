# encoding: utf-8

# 既然要获取最大的profit,那么只要选择每次price上升的时候卖出就可以了,
# 如果不是, 那么价格下降了,就失去了一部分的profit

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                profit += prices[i] - prices[i-1]

        return profit

if __name__ == '__main__':
    print Solution().maxProfit([7, 1, 4])



