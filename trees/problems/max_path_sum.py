from typing import Optional

from trees.problems.max_depth import TreeNode


def maxPathSum(self, root: Optional[TreeNode]) -> int:
    self.all_max = -10000

    def dfs(node):
        if node is None:
            return 0
        # only consider the left or right branch if they are non-negative
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))
        # check if the sum with node as root exceeds the current max
        self.all_max = max(self.all_max, node.val + left + right)
        # return the sum of node with max of left or right branch
        return node.val + max(left, right)

    root_max = dfs(root)
    return max(self.all_max, root_max)
