# encoding: utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.right), self.height(node.left)) + 1

    # 平衡二叉树: 左右子树的高度差<=1, 左子树是平衡二叉树, 右子树是平衡二叉树
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if abs(self.height(root.right) - self.height(root.left)) <= 1:
            if self.isBalanced(root.right) and self.isBalanced(root.left):
                return True
            else:
                return False
        else:
            return False







if __name__ == '__main__':
    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)
    e = TreeNode(6)

    root.right = a
    root.left = b
    a.right = c
    a.left = e
    c.left = d

    print Solution().isBalanced(a)





