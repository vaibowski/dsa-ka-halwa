from typing import Optional, List

from trees.problems.max_depth import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def bfs(node, level):
            if node is None:
                return
            if len(ans) <= level:
                ans.append([])
            ans[level].append(node.val)
            bfs(node.left, level+1)
            bfs(node.right, level+1)
            return

        bfs(root, 0)
        return ans
