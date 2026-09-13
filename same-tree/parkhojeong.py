# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if (p is None and q is not None) or (p is not None and q is None):
            return False

        if (p.left or q.left) and not self.isSameTree(p.left, q.left):
            return False

        if (p.right or q.right) and not self.isSameTree(p.right, q.right):
            return False

        return p.val == q.val

