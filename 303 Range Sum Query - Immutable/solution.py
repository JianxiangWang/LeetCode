# encoding: utf-8

# 构建辅助数组dp[i], 表示从0 -> i的和 ;   dp[i] = dp[i-1] + nums[i]
# ==> sumRange[i, j] = dp[j] - dp[i] + nums[i]
#
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums

        n = len(nums)
        if n == 0:
            return

        self.dp = [None] * n
        self.dp[0] = nums[0]
        for idx in range(1, n):
            self.dp[idx] = self.dp[idx-1] + nums[idx]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.nums == []:
            return 0

        return self.dp[j] - self.dp[i] + self.nums[i]



# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

if __name__ == '__main__':
    NumArray([-2, 0, 3, -5, 2, -1])