# Time Complexity: O(N) - visit each node once.
# Space Complexity: O(N) - skewed tree, recursion goes N levels deep.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root  # If the tree is empty, just return None.
        
        # swap left and right child nodes.
        root.left, root.right = root.right, root.left
        
        # recursively invert left and right subtrees.
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        
        return root
