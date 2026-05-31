# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # https://stackoverflow.com/a/37300370
        return self.isValid(root, float('-inf'), float('inf'))

    def isValid(self, node: Optional[TreeNode], low: float, high: float):
        if node is None:
            return True
        if node.val <= low or node.val >= high:
            return False
        return self.isValid(node.left, low, node.val) and self.isValid(node.right, node.val, high)
