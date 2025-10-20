# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        
        dfs(root)
        return values[k-1]
    
"""
이진 탐색 트리는 왼쪽은 val보다 작고 오른쪽은 val보다 큼
그렇기에 중위순회 방식으로 하면 자연스럽게 정렬된 상태로 배열에 들어가게 된다.
"""
