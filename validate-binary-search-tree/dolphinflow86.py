# 1) Validate the BST using min and max values for each node. 
# TC: O(N) where N is the number of nodes in the BST
# SC: O(H) where H is the height of the BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node: Optional[TreeNode], min: int, max: int) -> bool:
        if node == None: return True

        if node.val <= min or node.val >= max: return False

        left = self.solve(node.left, min, node.val)
        right = self.solve(node.right, node.val, max)
        return left and right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root, float('-inf'), float('inf'))