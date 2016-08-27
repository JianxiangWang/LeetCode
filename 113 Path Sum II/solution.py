# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        import copy

        ans = []

        def dfs(node, visited, ans):

            if node is None:
                return

            visited = copy.deepcopy(visited)
            visited.append(node.val)
            if node.left is None and node.right is None:
                s = 0
                for x in visited:
                    s += x
                if s == sum:
                    ans.append(visited)

            dfs(node.left, visited, ans)
            dfs(node.right, visited, ans)

        dfs(root, [], ans)

        return ans








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


    print Solution().pathSum(root, 9)


