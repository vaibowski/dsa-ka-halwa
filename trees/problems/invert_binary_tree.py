from typing import Optional

from trees.problems.max_depth import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        temp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = temp

        return root
