from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        - Idea: 두 트리는 구조가 같고, 각 노드의 값이 같아야 같은 트리라고 간주한다.
            이를 확인하기 위해 재귀적으로 각 노드를 비교한다.
        - Time Complexity: O(n). n은 트리의 노드 수.
            두 트리의 모든 노드를 비교해야 하므로 O(n)이 소요된다.
        - Space Complexity: O(n). n은 리스트의 노드 수.
            재귀 호출로 인해 호출 스택을 위한 공간이 필요하며, 최악의 경우 O(n)까지 필요할 수 있다.
        """

        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        is_left_equal = self.isSameTree(p.left, q.left)
        is_right_equal = self.isSameTree(p.right, q.right)

        return is_left_equal and is_right_equal
