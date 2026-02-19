"""
572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/

Solution:
    1) root의 각 노드에서 subRoot와 동일한 트리인지 확인
    2) 동일한 트리를 찾으면 True 반환
    3) 찾지 못하면 root의 왼쪽/오른쪽 서브트리에서 계속 탐색

    sameTree() 헬퍼 함수:
    - 두 트리의 구조와 값이 정확히 같은지 확인
    - 둘 다 None이면 True
    - 하나만 None이거나 val이 다르면 False
    - 왼쪽과 오른쪽 서브트리도 모두 같아야 True

Time: O(n * m) - n은 root의 노드 수, m은 subRoot의 노드 수
Space: O(min(n, m)) - 재귀 스택의 깊이
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # subRoot가 None이면 항상 subtree임
        if not subRoot:
            return True
        # root가 None이면 subRoot를 찾을 수 없음
        if not root:
            return False

        # 현재 노드에서 같은 트리인지 확인
        if self.sameTree(root, subRoot):
            return True

        # 아니면 왼쪽 또는 오른쪽 서브트리에서 탐색
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        """두 트리가 구조와 값이 같은지 확인"""
        # 둘 다 None이면 같은 트리
        if not s and not t:
            return True

        # 하나만 None이거나 val이 다르면 다른 트리
        if not s or not t or s.val != t.val:
            return False

        # 왼쪽과 오른쪽 서브트리도 모두 같아야 함
        return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
