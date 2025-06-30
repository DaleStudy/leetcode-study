# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # DFS
        # 시간복잡도 최악 O(n)/ 공간복잡도 O(log n) ~ O(n) (재귀깊이)
        self.count = 0
        self.answer = None

        def dfs(node):
            if not node:
                return

            # 가장 작은 값부터(왼쪽서브트리) 재귀로 탐색
            dfs(node.left)

            self.count += 1

            # k번째 작은 값 찾으면 바로 종료하기
            if self.count == k:
                self.answer = node.val
                return

            # 오른쪽 서브트리 탐색
            dfs(node.right)

        dfs(root)

        return self.answer
