from typing import Optional

from trees.problems.max_depth import TreeNode


def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    self.k = k
    self.res = 0

    # trick is to only do inorder traversal till you encounter the kth element,
    # since inorder traversal access elements in sorted order
    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        inorder(node.right)
        return

    inorder(root)
    return self.res
