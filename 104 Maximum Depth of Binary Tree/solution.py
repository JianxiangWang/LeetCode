# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, depth, ans):
            if node is None:
                return

            depth += 1
            if node.right is None and node.left is None:
                ans.append(depth)

            dfs(node.right, depth, ans)
            dfs(node.left, depth, ans)

        ans = []
        dfs(root, 0, ans)
        return max(ans) if ans != [] else 0

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

    print Solution().maxDepth(root)
