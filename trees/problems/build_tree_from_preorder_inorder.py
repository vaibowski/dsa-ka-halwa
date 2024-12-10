from typing import List, Optional

from trees.problems.max_depth import TreeNode


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if inorder:
        idx = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[idx])
        root.left = buildTree(preorder, inorder[0:idx])
        root.right = buildTree(preorder, inorder[idx + 1:])
        return root
