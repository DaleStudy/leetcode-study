# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# idea : dfs
# Time Complexity : O(n)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        tmp = root.left
        root.left = root.right 
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


