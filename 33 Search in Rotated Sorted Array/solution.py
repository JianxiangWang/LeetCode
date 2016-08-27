#encoding: utf-8

# 4 5 6 7 0 1 2
# binary search, always !
# low-mid or mid-high 之间始终有一个是有序的, 所以每一次都可以判断是target 在 low-mid 还是 high-mid 之间 !
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1

        found = -1
        while low <= high:

            print low, high

            mid = (low + high) >> 1

            if nums[mid] == target:
                found = mid
                break

            if nums[mid] > target:
                if nums[low] <= nums[mid]:
                    if target >= nums[low]:
                        high = mid - 1
                    else:
                        low = mid + 1

                if nums[mid] < nums[high]:
                    high = mid - 1

            if nums[mid] < target:
                if nums[low] <= nums[mid]:
                    if target >= nums[low]:
                        low = mid + 1

                if nums[mid] < nums[high]:
                    if target <= nums[high]:
                        low = mid +1
                    else:
                        high = mid - 1


        return found

if __name__ == '__main__':
    print Solution().search([4,5,6,7,8,0,1,2,3], 5)




