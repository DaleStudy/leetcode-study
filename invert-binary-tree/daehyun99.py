# Time: O(N)
# Space: O(H)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(node):
            if node is not None:
                node.left, node.right = bfs(node.right), bfs(node.left)
            return node
        return bfs(root)                
