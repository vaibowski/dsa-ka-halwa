from typing import Optional
from trees.problems.max_depth import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return depth(root) != -1
