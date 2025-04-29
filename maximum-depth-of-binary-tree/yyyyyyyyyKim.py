# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # DFS, 재귀
        def dfs(root):
            # 노드가 없으면 깊이 0
            if not root:
                return 0
            
            # 왼쪽과 오른쪽 중 더 깊은 쪽 + 1 리턴
            return 1 + max(dfs(root.left), dfs(root.right))
        
        return dfs(root)
