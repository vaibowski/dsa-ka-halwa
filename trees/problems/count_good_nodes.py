from trees.problems.max_depth import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, pathMax):
            if node is None:
                return
            if node.val >= pathMax:
                self.count += 1
                pathMax = node.val
            dfs(node.left, pathMax)
            dfs(node.right, pathMax)
            return

        dfs(root, root.val)
        return self.count