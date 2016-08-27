# encoding: utf-8

# 可以看做爬楼梯问题, amount 是目标, coins是你的各种能力
# dp[i]表示到i的最小数字数量
# dp[i] = min([dp[i-coin] for coin in coins if i-coins >=0 and dp[i-coin] != None]) + 1
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [None] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            tmp = [dp[i-coin] for coin in coins if i - coin >= 0 and dp[i-coin] != None]
            if tmp != []:
                dp[i] = min(tmp) + 1

        return dp[-1] if dp[-1] != None else -1

if __name__ == '__main__':
    print Solution().coinChange([3, 2], 1)


