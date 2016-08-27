#encoding: utf-8


# 状态转移
# dp[i] 表示以i位置结尾的 最长递增子序列的长度
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0

        dp = [None] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            tmp = [dp[j] + 1 for j in range(i) if nums[i] > nums[j]]
            if tmp == []:
                dp[i] = 1
            else:
                dp[i] = max(tmp)
        return max(dp)

if __name__ == '__main__':
    print Solution().lengthOfLIS([10,9,2,5,3,7,101,18])