#encoding: utf-8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        i = 0
        j = 0
        while i < n:

            while i < n-1 and nums[i] == nums[i+1]:
                i += 1
            nums[j] = nums[i]
            j += 1
            i += 1

        return j

if __name__ == '__main__':
    nums = [1, 1, 2, 3, 4, 4, 5]
    print Solution().removeDuplicates(nums)
    print nums