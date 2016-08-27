class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        def dfs(seq, ans, res):

            for x in seq:
                ans_ = ans + [x]
                tmp = [i for i in seq if i != x]

                if tmp == []:
                    res.append(ans_)

                dfs(tmp, ans_, res)

        res = []
        seq = range(1, n+1)
        dfs(seq, [], res)

        return res

if __name__ == '__main__':
    print Solution().getPermutation(9, 0)


