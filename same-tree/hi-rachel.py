from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
재귀 풀아
TC: O(N), 양 트리의 각 노드를 상대로 재귀함수를 딱 1번씩만 호출하기 때문
SC: O(N), 공간복잡도 = 콜스택의 최대 높이(노드의 수) 
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 둘 다 null이면 True 반환
        if not p and not q:
            return True
        # 둘 중 하나면 null이면 False 반환
        if not p or not q:
            return False
        # val이 서로 다르면 탐색 중단, False 반환
        if p.val != q.val:
            return False
        # 현재 node의 val이 같다면, 좌우측 자식 트리도 같은지 확인 -> 재귀 호출
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


"""
스택 풀이
TC: O(N)
SC: O(N)
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            p, q = stack.pop()
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            stack.append((p.left, q.left))
            stack.append((p.right, q.right))
        return True
