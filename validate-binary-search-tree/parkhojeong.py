# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, ~sys.maxsize, sys.maxsize)

    def dfs(self, root, min_val, max_val) -> bool:
        val = root.val
        if val <= min_val or val >= max_val:
            return False

        if root.left:
            if not self.dfs(root.left, min_val, val):
                return False
        if root.right:
            if not self.dfs(root.right, val, max_val):
                return False

        return True

