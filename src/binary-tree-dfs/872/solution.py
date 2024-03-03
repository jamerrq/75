from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        leafs1 = []
        leafs2 = []

        def aux(node, list_ref):
            if node is None:
                return
            if node.left is None and node.right is None:
                list_ref.append(node.val)

            aux(node.left, list_ref)
            aux(node.right, list_ref)

        aux(root1, leafs1)
        aux(root2, leafs2)

        return leafs1 == leafs2
