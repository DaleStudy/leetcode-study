'''
# 226. Invert Binary Tree

switch left and right child of each node

## TC: O(N)

visit each node once

## SC: O(h)

h is height of tree

- best case: O(logN), balanced tree
- worst case: O(N), skewed tree
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
