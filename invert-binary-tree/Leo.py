# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        else:
            root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)

        return root

        ## TC: O(n), SC: O(n), avg O(logn) if the given tree is balanced
