from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return traverse(node.left, low, node.val) and traverse(node.right, node.val, high)

        return traverse(root, float("-inf"), float("inf"))
