from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def aux(node, left=False, curr=0):
            # base case 1: no node
            if node is None:
                return curr

            nxt = node.left if left else node.right
            tmp = node.left if not left else node.right
            opt_in = aux(nxt, not left, curr + int(bool(nxt)))
            opt_out = aux(tmp, left, int(bool(tmp)))
            return max(opt_in, opt_out)

        left = aux(root, True)
        right = aux(root, False)
        return max(left, right)
