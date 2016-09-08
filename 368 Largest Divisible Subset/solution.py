#!/usr/bin/env python
#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# sort
# dp[i] 表示以nums[i]为最大值的最大可除子集的大小
# 状态转移
# dp[i]: num[i] % nums[j] == 0 and dp[j] +1 > dp[i];  j=1..i-1

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return []

        nums = sorted(nums)
        N = len(nums)
        dp = [1] * N
        pre = [None] * N

        for i in range(N):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    pre[i] = j

        # get the max
        idx = dp.index(max(dp))
        ans = []
        while idx is not None:
            ans.append(nums[idx])
            idx = pre[idx]
        return ans

        # nums = sorted(nums)
        # size = len(nums)
        # dp = [1] * size
        # pre = [None] * size
        # for x in range(size):
        #     for y in range(x):
        #         if nums[x] % nums[y] == 0 and dp[y] + 1 > dp[x]:
        #             dp[x] = dp[y] + 1
        #             pre[x] = y
        # idx = dp.index(max(dp))
        # ans = []
        # while idx is not None:
        #     ans += nums[idx],
        #     idx = pre[idx]
        # return ans


if __name__ == '__main__':
    # print Solution().largestDivisibleSubset([1, 2, 3])

    while 0:
        print 1




