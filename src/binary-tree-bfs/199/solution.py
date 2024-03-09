from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #
        def aux(node, lvl=0, tmp=[]):
            if node is None:
                return tmp

            # save the val in the tmp[lvl] position

            # if there is no tmp[lvl] position, push a []
            # into the tmp
            nval = node.val
            if len(tmp) < lvl + 1:
                tmp.append(nval)

            else:
                tmp[lvl] = nval

            aux(node.left, lvl + 1, tmp)
            aux(node.right, lvl + 1, tmp)

        ans = []
        aux(root, tmp=ans)
        return ans
