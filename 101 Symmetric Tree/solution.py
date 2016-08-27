# encoding: utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    # 判断两颗子树是否对称
    # ==> 判断当前两个节点是否相等, 判断其对应的子树是否相等
    def helper(self, p, q):
        if p is None and q is None:
            return True

        if p and q and p.val == q.val:
            if self.helper(p.left, q.right) and self.helper(p.right, q.left):
                return True

        return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.helper(root.left, root.right)
        return True

