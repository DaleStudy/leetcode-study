# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        max_depth = 0
        def dfs(cur_node, cur_depth):
            nonlocal max_depth
            if cur_node == None:
                return 
            cur_depth += 1
            max_depth = max(max_depth, cur_depth)

            dfs(cur_node.left, cur_depth)
            dfs(cur_node.right, cur_depth)
            return
        
        dfs(root, 0)
        return max_depth
      
