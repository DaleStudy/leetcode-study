'''
Time Complexity: O(N)
- dfs 함수가 모든 노드를 중위순회 방식으로 방문함므로 O(N) 소요

Space Complexity: O(N)
- aligned_arr 리스트에 모든 노드의 값을 저장하므로 O(N) 소요
- 재귀 호출 스택이 최대 트리의 높이만큼 쌓일 수 있으므로 최악의 경우 O(N) 소요
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        aligned_arr = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            aligned_arr.append(node.val)
            dfs(node.right)
        
        dfs(root)

        return aligned_arr[k - 1]
