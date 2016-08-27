# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        res = []
        nodes = [root]
        level = 0

        while nodes:
            tmp = [node.val for node in nodes]
            if level % 2 == 1:
                tmp = tmp[::-1]
            res.append(tmp)

            next_nodes = []
            for node in nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)

            nodes = next_nodes
            level += 1

        return res

