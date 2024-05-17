# TC: O(n), SC:O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    t = []
    def pre_order(self, node: TreeNode):
        if node is None:
            self.t.append(None)
            return

        self.t.append(node.val)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.t = []
        self.pre_order(p)
        a = self.t[:]
        self.t = []
        self.pre_order(q)
        b = self.t[:]

        return a == b
