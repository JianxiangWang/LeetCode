# encoding: utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if p is None or q is None:
            return root

        # 使用dfs得到root到p, q 的路经
        def dfs(node, visited, res):
            if node is None:
                return

            visited_ = visited + [node]
            if node == p or node == q:
                res.append(visited_)

            dfs(node.left, visited_, res)
            dfs(node.right, visited_, res)

        res = []
        dfs(root, [], res)

        i = 0
        for idx in range(min(len(res[0]), len(res[1]))):
            if res[0][idx] == res[1][idx]:
                i += 1
            else:
                return res[0][i - 1]

        return res[0][i - 1]

    def findPath(self, root, target):
        stack = []
        lastVisit = None
        while stack or root:

            for x in stack:
                print x.val,

            if root:
                stack.append(root)
                root = root.left
            else:
                peek = stack[-1]
                if peek.right and lastVisit != peek.right:
                    root = peek.right
                else:
                    if peek == target:
                        return stack
                    lastVisit = stack.pop()
                    root = None
        return stack

if __name__ == '__main__':
    root = TreeNode(0)
    a = TreeNode(1)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)
    e = TreeNode(6)

    root.left = a
    root.right = b
    a.left = c
    a.right = d
    c.left = e

    for x in Solution().findPath(root, e):
        print x.val
