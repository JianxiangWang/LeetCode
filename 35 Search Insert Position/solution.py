
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n-1

        found = -1
        while low <= high:
            mid = (low + high) >> 1

            if nums[mid] == target:
                found = mid
                break

            if nums[mid] > target:
                high = mid - 1

            if nums[mid] < target:
                low = mid +1

        print low, high
        if found != -1:
            return found
        else:
            return low

if __name__ == '__main__':
    print Solution().searchInsert([1,3,5,6], 0)
