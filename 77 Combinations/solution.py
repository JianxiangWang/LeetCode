# encoding: utf-8

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def dfs(nodes, index, depth, comb, res):

            if depth == k:
                res.append(comb)
                return

            # 过了这深度, 我不要
            if depth > k:
                return

            # 从这个点开始, 无法达到深度K, 不要
            if depth + n - index < k:
                return

            for i in range(index, len(nodes)):

                dfs(nodes, i+1, depth +1, comb + [nodes[i]], res)


        res = []
        nodes = range(1, n+1)
        dfs(nodes, 0, 0, [], res)

        return res

if __name__ == '__main__':
     print Solution().combine(4, 2)
