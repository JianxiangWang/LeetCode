# encoding: utf-8


# 可以看作是一个爬楼梯的问题
#  dp[i] = sum([dp[i-num] for num in nums if i - num >= 0 ])
#  要达到i, 可以通过 i-num 跨 num 过来
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        dp = [None] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            dp[i] = sum([dp[i-num] for num in nums if i - num >= 0])

        return dp[-1]


if __name__ == '__main__':
    print Solution().combinationSum4([1, 2, 3], 4)
