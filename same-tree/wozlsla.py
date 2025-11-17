from typing import Optional

"""
# Intuition
어떻게 순서가 정의되지?
순회 -> 어떤 구조?
비교

# Approach
트리가 동일하려면 ?
    1. 구조 비교
    2. 값 비교

트리 동시 탐색
    - 두 노드가 모두 null (구조) -> True
    - 둘 중 하나만 null (구조) -> False
    - 두 노드가 모두 값이 있음 (값) -> True/False

# Complexity
시간 복잡도
    - O(N)
공간 복잡도
    - (재귀) 전위 순회: 콜 스택 -> O(H)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # 종결 조건 1: 두 노드가 모두 null이면 구조가 동일함
        if p is None and q is None:
            return True

        # 종료 조건 2:
        # - 구조 불일치
        # - 값 불일치
        if p is None or q is None or p.val != q.val:
            return False

        # (재귀) 자식 비교
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
