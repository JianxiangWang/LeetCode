# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        self.flag = False

        def dfs(node, s):
            if node is None:
                return
            s += node.val
            if node.left is None and node.right is None:
                if s == sum:
                    self.flag = True

            dfs(node.left, s)
            dfs(node.right, s)

        dfs(root, 0)

        return self.flag






if __name__ == "__main__":

    root = TreeNode(5)
    a = TreeNode(3)
    b = TreeNode(1)
    c = TreeNode(1)
    d = TreeNode(7)
    e = TreeNode(4)
    f = TreeNode(2)

    root.right = a
    root.left = d
    a.right = b
    a.left = c
    d.right = e
    d.left = f


    print Solution().hasPathSum(root, 1)


