"""
# Approach
재귀를 이용해서 왼쪽, 오른쪽 서브트리의 값을 비교합니다

# Complexity
- Time complexity: 노드 개수 N일 때, O(N)
- Space complexity: 트리 높이 H 일때, O(H)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
