
# [0, 1, 0, 3, 12] ==> [1, 3, 12, 0, 0]
class Solution(object):
    # 112ms
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        prev_j = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                for j in range(prev_j+1, i):
                    if nums[j] == 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        prev_j = j
                        break

    # 104ms
    def moveZeroes_2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        for x in range(j, len(nums)):
            nums[x] = 0




if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print nums





