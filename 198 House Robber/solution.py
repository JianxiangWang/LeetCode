# encoding: utf-8

# 状态转移方程
# dp[i] = max(dp[i-1], dp[i-2] + num[i])
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
        if nums == []:
            return 0

        dp = [None] * len(nums)

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for idx in range(2, len(nums)):
            dp[idx] = max(dp[idx-1], dp[idx - 2] + nums[idx])

        return dp[-1]


if __name__ == '__main__':
    print Solution().rob([1, 4, 9, 7, 1, 2, 39999944, 5, 5])