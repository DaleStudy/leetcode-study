# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root: Optional[TreeNode], minimum: int, maximum: int) -> bool:
        if root is None:
            return True

        if root.val <= minimum or root.val >= maximum:
            return False

        return self.check(root.left, minimum, root.val) and self.check(root.right, root.val, maximum)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minimum_constraint = ((-2) ** 31) - 1
        maximum_constraint = 2 ** 31

        return self.check(root, minimum_constraint, maximum_constraint)
