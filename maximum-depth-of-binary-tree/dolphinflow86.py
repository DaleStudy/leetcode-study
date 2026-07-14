# 1) Use DFS to traverse down to the leaf node. Keep track of depth and return each node's maximum depth of each subtree to the parent node.
# TC: O(N) where N is the number of node in the binary tree
# SC: O(H) where H is the height of the binary tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode], depth: int) -> int:
        if not node:
            return depth

        left = self.dfs(node.left, depth + 1)
        right = self.dfs(node.right, depth + 1)
        return max(left, right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
