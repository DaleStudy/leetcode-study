# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

"""
================================================================================
풀이 과정
================================================================================

[1차 시도] 재귀로 깊이 카운트 - None은 0
────────────────────────────────────────────────────────────────────────────────
1. 빈 노드(None)는 깊이가 0이
2. leaf 노드에서 양쪽 자식이 None이면 둘 다 0을 반환
3. 그러면 leaf 노드는 max(0, 0) + 1 = 1이 됨 (자기 자신만 카운트)

        def maxDepth(self, root):
            if not root:
                return 0  # 빈 노드는 0

            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

            return max(left, right) + 1  # 더 깊은 쪽 + 나 자신(1)

4. 동작 예시:
   트리:     1
           / \
          2   3
         /
        4

   maxDepth(4) → max(0, 0) + 1 = 1
   maxDepth(2) → max(1, 0) + 1 = 2
   maxDepth(3) → max(0, 0) + 1 = 1
   maxDepth(1) → max(2, 1) + 1 = 3 ✓


5. 시간복잡도: O(n) - 모든 노드를 1번씩 방문
6. 공간복잡도: O(h) - 재귀 스택, h는 트리 높이
"""
