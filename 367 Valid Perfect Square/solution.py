# encoding: utf-8

# 定义有序的搜索域
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return  True

        target = num
        low = 0
        high = num / 2
        found = False
        while low <= high:
            mid = (low + high) >> 1

            val = mid **2
            if val == target:
                found = True
                break
            if val < target:
                low = mid + 1
            if val > target:
                high = mid - 1

        return found

if __name__ == '__main__':
    print Solution().isPerfectSquare(16)
