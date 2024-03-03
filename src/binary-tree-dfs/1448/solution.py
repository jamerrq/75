# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def aux(self, root: TreeNode, curr_max) -> int:
        if root is None:
            return 0

        this_counts = int(root.val >= curr_max)
        curr_max = max(root.val, curr_max)
        return this_counts + \
         self.aux(root.left, curr_max) + \
         self.aux(root.right, curr_max)
    def goodNodes(self, root: TreeNode) -> int:
        return self.aux(root, float('-inf'))
