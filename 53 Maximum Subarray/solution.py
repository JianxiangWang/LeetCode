class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        dp = [None] * len(nums)
        dp[0] = nums[0]

        max_sum = dp[0]
        for idx in range(1, len(nums)):
            dp[idx] = max(dp[idx-1] + nums[idx], nums[idx])

            if dp[idx] > max_sum:
                max_sum = dp[idx]

        return max_sum


if __name__ == '__main__':
    print Solution().maxSubArray([-2, 1,-3,4,-1,2,1,-5,4])