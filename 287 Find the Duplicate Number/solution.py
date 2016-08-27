#encoding: utf-8

class Solution(object):
    # def findDuplicate(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #
    #     s = set()
    #     for x in nums:
    #         if x in s:
    #             return x
    #         else:
    #             s.add(x)


    # 因为数字都在 1...n 之间, 可以在1..n上使用二分查找
    # mid, 如果<=mid的数的个数大于mid, 则在low, mid 之间继续查找
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        low = 1
        high = len(nums) - 1

        while low < high:
            mid = (low + high) / 2

            print low, mid, high

            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid+1

        return low










if __name__ == '__main__':
    print Solution().findDuplicate([1, 2, 2])