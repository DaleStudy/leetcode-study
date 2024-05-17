"""
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/description/

Solution
    Recursively swaps the left and right children of the root node.

    1. Check if the root has left and right children.
    2. If it does, invert the left and right children.
    3. If it doesn't, invert the left or right child.
    4. Return the root.

Time complexity: O(n)
Space complexity: O(n)

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        has_left = hasattr(root, "left")
        has_right = hasattr(root, "right")

        if has_left and has_right:
            root.left, root.right = self.invertTree(root.right), self.invertTree(
                root.left
            )
        elif has_left:
            root.left, root.right = None, self.invertTree(root.left)
        elif has_right:
            root.left, root.right = self.invertTree(root.right), None

        return root
