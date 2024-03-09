from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def aux(node, tmp=[], lvl=0):
            if node is None:
                return tmp

            nval = node.val
            if len(tmp) < lvl + 1:
                tmp.append(0)

            tmp[lvl] += nval
            aux(node.left, tmp, lvl + 1)
            aux(node.right, tmp, lvl + 1)

        sums = []
        aux(root, sums)
        ans = -float('inf')
        lvl = -1
        for i in range(len(sums)):
            if sums[i] > ans:
                ans = sums[i]
                lvl = i + 1

        return lvl
