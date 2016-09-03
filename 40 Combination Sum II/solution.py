class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        def dfs(candidates, target, index, combination, ans):
            if target == 0:
                ans.append(combination)
                return
            if target < 0:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                dfs(candidates, target - candidates[i], i+1, combination + [candidates[i]], ans)


        ans = []
        dfs(candidates, target, 0, [], ans)

        return ans



# }

if __name__ == '__main__':
    print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)

