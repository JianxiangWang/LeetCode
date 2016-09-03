class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        candidates = range(1, 10)

        def dfs(candidates, target, index, depth, combination, res):

            if target == 0 and depth == k:
                res.append(combination)
                return
            if target < 0:
                return
            if depth > k:
                return

            for i in range(index, len(candidates)):
                dfs(candidates, target - candidates[i], i+1, depth+1, combination+[candidates[i]], res)


        res = []
        dfs(candidates, n, 0, 0, [], res)
        return res

if __name__ == '__main__':
    print Solution().combinationSum3(3, 7)

