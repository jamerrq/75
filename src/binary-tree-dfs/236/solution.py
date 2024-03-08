# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def aux(node, target, path=""):
            if node is None:
                return False, path

            new_path = path + ',' + str(node.val)

            if node.val == target:
                return True, new_path

            left, path1 = aux(node.left, target, new_path)
            right, path2 = aux(node.right, target, new_path)

            if left:
                return True, path1
            if right:
                return True, path2

            return False, ''

        def find_node(node, target):
            if node is None or node.val == target:
                return node
            op1 = find_node(node.left, target)
            if op1 is not None:
                return op1
            return find_node(node.right, target)

        _, path_p = aux(root, p.val)
        _, path_q = aux(root, q.val)

        print(path_p, path_q)
        pp = list(map(lambda x: int(x), path_p.split(',')[1:]))
        pq = list(map(lambda x: int(x), path_q.split(',')[1:]))

        l = -1
        for i in range(min(len(pp), len(pq))):
            if pp[i] == pq[i]:
                l = pp[i]
            else:
                break

        return find_node(root, int(l))
