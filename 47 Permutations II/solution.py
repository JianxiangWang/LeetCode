
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(seq, ans, res):

            seq = sorted(seq)
            prev_x = None
            for idx, x in enumerate(seq):

                if x == prev_x:
                    continue
                prev_x = x

                ans_ = ans + [x]
                tmp = seq[:idx] + seq[idx + 1:]
                if tmp == []:
                    res.append(ans_)

                dfs(tmp, ans_, res)

        res = []
        dfs(nums, [], res)

        return  res
        # return list(map(list, set(res)))

if __name__ == '__main__':
    print Solution().permuteUnique([3, 3, 0, 3])