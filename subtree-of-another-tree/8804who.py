# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def getTreeNodes(node):
            if not node:
                return "#"
            
            return ":"+str(node.val)+":"+getTreeNodes(node.left)+getTreeNodes(node.right)

        
        return getTreeNodes(subRoot) in getTreeNodes(root)
    
