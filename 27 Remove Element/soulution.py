# encoding: utf-8

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        n = len(nums)
        i = 0
        j = n - 1

        # i 指向第一个为val的
        while i < n:
            if nums[i] == val:
                break
            i += 1

        # j 指向第一个不为val的
        while j >= 0:
            if nums[j] != val:
                break
            j -= 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            res = j


            # i 指向第一个为val的
            while i < n:
                if nums[i] == val:
                    break
                i += 1

            # j 指向第一个不为val的
            while j >= 0:
                if nums[j] != val:
                    break
                j -= 1

        return j+1

if __name__ == '__main__':
    nums = [2,2,2 ]
    print Solution().removeElement(nums, 2)
    print nums



