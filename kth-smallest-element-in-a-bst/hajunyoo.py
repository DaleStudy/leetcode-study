# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    # Time complexity: O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = 0

        def dfs(node):
            if not node:
                return

            dfs(node.left)

            self.count += 1
            if self.count == k:
                self.result = node.val
                return

            dfs(node.right)

        dfs(root)
        return self.result
