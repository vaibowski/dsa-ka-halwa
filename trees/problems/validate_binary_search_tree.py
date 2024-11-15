import sys
from typing import Optional

from trees.problems.max_depth import TreeNode


def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def dfs(node, mini, maxi):
        if node is None:
            return True
        if node.val <= mini or node.val >= maxi:
            return False
        leftMax = node.val
        rightMin = node.val

        return dfs(node.left, mini, leftMax) and dfs(node.right, rightMin, maxi)

    return dfs(root, -sys.maxsize, sys.maxsize)


def isValidBSTInorderTraversal(self, root: Optional[TreeNode]) -> bool:
    output = []

    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        output.append(node.val)
        inorder(node.right)
        return

    inorder(root)

    for i in range(1, len(output)):
        if output[i - 1] >= output[i]:
            return False

    return True
