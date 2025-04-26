"""
시간 복잡도: O(N)
공간 복잡도: O(h) h = 트리 높이
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(tree: Optional[TreeNode], depth: int):
            nonlocal result
            if tree == None:
                result = max(result, depth)
                return
            
            dfs(tree.left, depth + 1)
            dfs(tree.right, depth + 1)
        
        dfs(root, 0)
        return result
