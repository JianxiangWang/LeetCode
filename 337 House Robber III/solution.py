# encoding: utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 动态规划 + dfs
class Solution(object):

    # dict_node_to_rob = {}
    # def rob(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if root is None:
    #         return 0
    #
    #     if root in self.dict_node_to_rob:
    #         return self.dict_node_to_rob[root]
    #
    #
    #     # 不抢root节点
    #     a = self.rob(root.left) + self.rob(root.right)
    #     # 抢root节点
    #     b = root.val
    #     if root.right:
    #         b += self.rob(root.right.right) + self.rob(root.right.left)
    #     if root.left:
    #         b += self.rob(root.left.right) + self.rob(root.left.left)
    #
    #     self.dict_node_to_rob[root] = max(a, b)
    #     return max(a, b)
    #

    # 每个节点保留2个数值
    # 1: 不抢当前节点, 获得的最大有收益
    # 2: 抢当前节点,获得的最大收益
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        a, b = self.helper(root)

        return max(a, b)


    def helper(self, node):

        if node is None:
            return 0, 0

        left_0, left_1 = self.helper(node.left)
        right_0, right_1 = self.helper(node.right)

        # 不抢当前节点
        a = max(left_0, left_1) + max(right_0, right_1)
        # 抢当前节点
        b = node.val + left_0 + right_0
        return a, b



