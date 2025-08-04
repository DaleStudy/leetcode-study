"""
https://leetcode.com/problems/subtree-of-another-tree/description/

두 개의 이진 트리 root와 subRoot의 루트(최상위 노드)가 주어졌을 때,
root의 하위 트리 중 subRoot와 동일한 구조와 값이 있는 경우 참을 반환하고 그렇지 않은 경우 거짓을 반환

TC: O(n * m), n: root의 노드 수, m: subRoot의 노드 수
SC: O(n + m)
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
        if not root:
            return False
        if not subRoot:
            return True
       
        def isSameTree(p, q):
            # 둘 중 하나라도 None 이면,
            if not p or not q:
                # 둘 다 None 일 때만 True
                return not p and not q
            # 같이 다르면 False
            if p.val != q.val:
                return False
            # 왼쪽과 오른쪽 서브트리를 재귀적으로 비교
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        # root에서 시작해 subRoot와 동일한 구조의 트리인지 확인
        if isSameTree(root, subRoot):
            return True

        # 왼쪽 또는 오른쪽 서브트리 중 하나라도 subRoot와 같은 트리가 있는지 재귀 탐색
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
