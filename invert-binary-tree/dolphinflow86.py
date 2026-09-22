# N is the number of nodes in the binary tree.
# TC: O(N) - visits each node exactly once
# SC: O(H) - uses the recursion stack proportional to tree height H

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def invertTree(self, root):
        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(
            root.left
        )

        return root
