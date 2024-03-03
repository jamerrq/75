from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def aux(node, current_sum = 0):
            if not node:
                return 0
            current_sum += node.val
            return (current_sum == targetSum) + aux(node.left, current_sum) + aux(node.right, current_sum)
        if not root:
            return 0
        return aux(root) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
