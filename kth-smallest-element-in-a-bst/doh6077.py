# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity O(N)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        final = 0 
        def dfs(node):
            nonlocal final
            if not node:
                return 
            dfs(node.left)
            ans.append(node.val)
            if len(ans) == k:
                final = node.val
            if len(ans) < k:
                dfs(node.right)
        dfs(root)
        return final
