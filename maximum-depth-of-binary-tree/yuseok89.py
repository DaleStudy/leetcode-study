# TC: O(N)
# SC: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def rec(node, height):
            if not node:
                return height

            return max(rec(node.left, height + 1), rec(node.right, height + 1))

        return rec(root, 0)

