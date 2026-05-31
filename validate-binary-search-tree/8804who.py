# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        def dfs(node, min_num, max_num):
            if not node:
                return True
            if max_num <= node.val or node.val <= min_num:
                return False       
            return dfs(node.left, min_num, node.val) and dfs(node.right, node.val, max_num)
        return dfs(root, float("-inf"), float("inf"))
    
