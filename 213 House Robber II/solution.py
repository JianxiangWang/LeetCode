#encoding: utf-8

# 打破环,分类讨论 !
# 1. 抢第一个, 则不能抢最后一个
# 2. 不抢第一个,则可以抢最后一个
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

        # 1. 抢第一个
        dp1 = [None] * len(nums)
        dp1[0] = nums[0]
        dp1[1] = nums[0]
        # 不能抢最后一个
        for idx in range(2, len(nums) - 1):
            dp1[idx] = max(dp1[idx-1], dp1[idx-2] + nums[idx])

        # 2. 不抢第一个
        dp2 = [None] * len(nums)
        dp2[0] = 0
        dp2[1] = nums[1]
        # 可以抢最后一个
        for idx in range(2, len(nums)):
            dp2[idx] = max(dp2[idx-1], dp2[idx-2] + nums[idx])

        return max(dp1[-2], dp2[-1])


if __name__ == '__main__':

    print Solution().rob([2,1,1,1])

