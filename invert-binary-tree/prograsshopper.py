# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time Complexity: O(N) / Space Complexity: O(N)
        if not root or (not root.left and not root.right):
            return root

        def invert(node: TreeNode):
            if not node:
                return
            node.right, node.left = node.left, node.right
            if node.right:
                invert(node.right)
            if node.left:
                invert(node.left)

        invert(root)
        return root
