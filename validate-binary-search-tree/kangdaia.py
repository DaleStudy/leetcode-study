from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checker(self, node: Optional[TreeNode], low: float, high: float) -> bool:
        """(Helper)
        주어진 노드가 유효한 BST 노드인지 검증하는 함수

        Args:
            node (Optional[TreeNode]): 검증할 node 객체
            low (float): node.val이 될 수 있는 최소값
            high (float): node.val이 될 수 있는 최대값

        Returns:
            bool: node가 유효한 BST 노드인지 여부
        """
        if node is None:
            return True
        value = node.val
        left, right = node.left, node.right
        if not (low < value < high):
            return False
        return self.checker(left, low, value) and self.checker(right, value, high)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        현재 트리가 올바른 binary tree인지 검증하는 함수

        checker 함수를 이용하여 트리의 모든 노드가 BST의 조건을 만족하는지 검증함.
        checker 함수는 재귀적으로 호출되고, 각 노드의 값이 허용된 범위 내에 있는지 확인함.
        이후 왼쪽 자식 노드는 현재 노드의 값보다 작은 범위로, 오른쪽 자식 노드는 현재 노드의 값보다 큰 범위로 검증함.

        Args:
            root (Optional[TreeNode]): 검증되지 않는 tree 객체

        Returns:
            bool: 올바른 binary tree인지 여부
        """
        return self.checker(root, -float("inf"), float("inf"))
