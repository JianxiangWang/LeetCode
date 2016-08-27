# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        def dfs(node, depth, ans):
            if node is None:
                return
            depth += 1
            if node.left is None and node.right is None:
                ans.append(depth)

            dfs(node.right, depth, ans)
            dfs(node.left, depth, ans)

        ans = []
        dfs(root, 0, ans)

        return min(ans)

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

    print Solution().minDepth(d)