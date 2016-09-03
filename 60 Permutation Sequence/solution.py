
# just math ~
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        k -= 1

        fac = 1
        for x in range(1, n):
            fac *= x

        res = []
        nums = range(1, n+1)
        for i in range(n)[::-1]:

            num = nums[k/fac]
            res.append(num)
            nums.remove(num)

            if i != 0:
                k = k % fac
                fac /= i

        return "".join(map(str, res))


if __name__ == '__main__':
    print Solution().getPermutation(1, 1)


