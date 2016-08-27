import copy



class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, ans, res):
            for x in nums:
                sub = set(nums) - {x}
                if len(sub) == 0:
                    ans_t = copy.deepcopy(ans)
                    ans_t.append(x)
                    res.append(ans_t)
                else:
                    ans_t = copy.deepcopy(ans)
                    ans_t.append(x)
                    dfs(sub, ans_t, res)

        res = []
        dfs(nums, [], res)
        return res

    def permute2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, ans, res):
            for x in nums:
                sub = set(nums) - {x}
                ans_t = copy.deepcopy(ans)
                ans_t.append(x)
                res.append(ans_t)

                dfs(sub, ans_t, res)

        res = []
        dfs(nums, [], res)
        return res

if __name__ == '__main__':
    print sorted(Solution().permute2([1, 2, 3, 4]), key=lambda x: len(x))
