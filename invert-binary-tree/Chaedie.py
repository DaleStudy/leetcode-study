"""
Time: O(n)
Space: O(n)
"""


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        temp = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(temp)

        return root
