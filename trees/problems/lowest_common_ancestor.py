from trees.problems.max_depth import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root
        # while both p and q lie on the same side of the root, this product will be > 0
        while (root.val - p.val) * (root.val - q.val) > 0:
            # we update root to the side both p and q lie on
            if p.val < root.val:
                root = root.left
            else:
                root = root.right

        return root
