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

