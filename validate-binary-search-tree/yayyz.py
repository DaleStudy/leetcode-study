# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_bst(node):
            if not node:
                return True, float('inf'), float('-inf')  # (is_bst, min_val, max_val)

            left_valid, left_min, left_max = is_bst(node.left)
            right_valid, right_min, right_max = is_bst(node.right)

            if not left_valid or not right_valid:
                return False, 0, 0

            if not (left_max < node.val < right_min):
                return False, 0, 0

            return True, min(left_min, node.val), max(right_max, node.val)

        valid, _, _ = is_bst(root)
        return valid        
