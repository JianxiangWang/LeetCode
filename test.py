import copy



class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                maxprofit += prices[i] - prices[i-1]
        return maxprofit


if __name__ == '__main__':
    print Solution().maxProfit([4, 1, 7])


