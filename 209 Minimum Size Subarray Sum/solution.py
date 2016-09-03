# encoding: utf-8

class Solution(object):

    # 二分查找
    # As to NLogN solution, logN immediately reminds you of binary search.
    # In this case, you cannot sort as the current order actually matters.
    # How does one get an ordered array then?
    # Since all elements are positive, the cumulative sum must be strictly increasing.
    # Then, a subarray sum can expressed as the difference between two cumulative sum.
    # Hence, given a start index for the cumulative sum array, the other end index can be searched using binary search.
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        sums = [0] * (len(nums) + 1)
        for i in range(1, len(nums)+1):
            sums[i] = sums[i-1] + nums[i-1]

        print sums


        minLen = len(nums) + 1
        for i in range(len(sums)):
            end = self.binarySearch(i+1, len(sums) - 1, sums[i] + s, sums)
            if end == len(sums):
                break
            if end - i < minLen:
                minLen = end - i

        return minLen if minLen != len(nums) + 1 else 0



    def binarySearch(self, low, high, key, sums):
        while low <= high:
            mid = (low + high) / 2
            if sums[mid] >= key:
                high = mid - 1
            else:
                low = mid + 1

        return low




if __name__ == '__main__':

    print Solution().minSubArrayLen(7, [2,3,1,2,4,3])