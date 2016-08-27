class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        nums = sorted(nums)
        n = len(nums)
        if n < 3:
            return []

        for i in range(n):
            if i == 0 or nums[i] != nums[i-1]:
                target = -nums[i]
                left = i + 1
                right = n - 1

                while left < right:
                    if nums[left] + nums[right] == target:
                        res.append([nums[i], nums[left], nums[right],])
                        #
                        while left < n-1 and nums[left] == nums[left+1]: left += 1
                        left += 1
                        while right >= 1 and nums[right] == nums[right-1]:right -= 1
                        right -= 1

                    if left < right and nums[left] + nums[right] > target:
                        while right >= 1 and nums[right] == nums[right-1]: right -= 1
                        right -= 1


                    if left < right and  nums[left] + nums[right] < target:
                        while left < n - 1 and nums[left] == nums[left + 1]: left += 1
                        left += 1

        return res

if __name__ == '__main__':
    print sorted([-1, 0, 1, 2, -1, -4])
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])


