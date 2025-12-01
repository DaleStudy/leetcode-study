# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # I think I should implement a depth first search
        self.max_level = 0
        def dps(root, level):
            if root == None:
                return 0
            level += 1
            self.max_level = max(self.max_level, level)
            if root.left:
                dps(root.left,level)
            if root.right:
                dps(root.right,level)

            return root
        dps(root,0)
        return self.max_level