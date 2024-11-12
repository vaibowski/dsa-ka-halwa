from typing import Optional, List

from trees.problems.max_depth import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []

        def bfs(node, level):
            if node is None:
                return
            if len(levels) <= level:
                levels.append([])
            levels[level].append(node.val)
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)

            return

        bfs(root, 0)
        ans = []
        for level in levels:
            ans.append(level[-1])

        return ans
