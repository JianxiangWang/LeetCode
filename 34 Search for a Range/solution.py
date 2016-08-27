class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        low = 0
        high = len(nums) - 1
        found_idx = -1
        while low <= high:
            mid = (low + high) / 2

            if nums[mid] > target:
                high = mid - 1
            if nums[mid] < target:
                low = mid + 1
            if nums[mid] == target:
                found_idx = mid
                break

        if found_idx == -1:
            return [-1, -1]

        i = found_idx
        while i >= 0 and nums[i] == target:
            i -= 1
        i += 1

        j = found_idx
        while j < len(nums) and nums[j] == target:
            j += 1
        j -= 1

        return [i, j]

if __name__ == '__main__':
    print Solution().searchRange([5, 7, 7, 8, 8, 10], 8)


