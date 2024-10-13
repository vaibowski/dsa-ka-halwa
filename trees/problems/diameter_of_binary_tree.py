from typing import Optional
from max_depth import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxd = 0

        def dfs(node):
            left = dfs(node.left) if node.left else 0
            right = dfs(node.right) if node.right else 0
            self.maxd = max(self.maxd, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.maxd
