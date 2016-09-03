class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(candidates, target, index, combination, ans):

            for i in range(index, len(candidates)):
                t = target - candidates[i]
                combination_ = combination + [candidates[i]]
                if t == 0:
                    ans.append(combination_)
                if t > 0:
                    dfs(candidates, t, i, combination_, ans)

        ans = []
        dfs(candidates, target, 0, [], ans)

        return ans

if __name__ == '__main__':
    print Solution().combinationSum([2, 3, 6, 7], 7)