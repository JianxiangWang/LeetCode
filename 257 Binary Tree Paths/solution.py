
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None






root = TreeNode("root")
a = TreeNode("a")
b = TreeNode("b")
c = TreeNode("c")
d = TreeNode("d")

root.left = a
root.right = b
a.left = c
c.right = d



def visit(treeNode, path, ans):

    if treeNode is None:
        return

    if path == "":
        path = treeNode.val
    else:
        path = path + "->" + treeNode.val

    if treeNode.left is None and treeNode.right is None:
       ans.append(path)

    visit(treeNode.left, path, ans)
    visit(treeNode.right, path, ans)

ans = []
visit(root, "", ans)
print ans


