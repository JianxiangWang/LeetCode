#encoding: utf-8

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 使用这种方式, 可以得到所有不同长度的, 不重复的组合!
        def dfs(nodes, index, comb, res):
            res.append(comb)
            for i in range(index, len(nodes)):
                dfs(nodes, i+1, comb+[nodes[i]], res)

        res = []
        dfs(nums, 0, [], res)
        return res

if __name__ == '__main__':
    print Solution().subsets([1, 2, 3])



    unicode("svsv", errors="ignore")

