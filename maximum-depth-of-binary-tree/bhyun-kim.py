"""
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Solution:
    This is a recursive problem that requires traversing the binary tree.
    We can use a recursive function to traverse the binary tree and calculate the depth.
    The depth of the binary tree is the maximum of the depth of the left and right subtrees.
    We can calculate the depth of the left and right subtrees recursively.
    The base case is when the root is None, in which case the depth is 0.
    
    1. Calculate the depth of the left subtree.
    2. Calculate the depth of the right subtree.
    3. Return the maximum of the depth of the left and right subtrees plus 1.

Time complexity: O(n)
Space complexity: O(n)
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_dep_left = 0
        max_dep_right = 0

        if hasattr(root, "left"):
            max_dep_left = 1 + self.maxDepth(root.left)
        if hasattr(root, "right"):
            max_dep_right = 1 + self.maxDepth(root.right)

        return max(max_dep_left, max_dep_right)
