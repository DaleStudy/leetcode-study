# TC: O(N)
# SC: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValid(self, left_bound, right_bound, root):
        if root is None:
            return True
        if left_bound is not None and left_bound >= root.val:
            return False
        if right_bound is not None and right_bound <= root.val:
            return False

        return self.isValid(left_bound, root.val, root.left) and self.isValid(root.val, right_bound, root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(None, root.val, root.left) and self.isValid(root.val, None, root.right)

