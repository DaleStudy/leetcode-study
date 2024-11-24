from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        - Idea: 각 노드 값의 허용 범위를 정하고 재귀적으로 검사한다.
            1. BST의 정의 활용
              왼쪽 서브트리의 모든 값은 현재 노드 값보다 작고, 오른쪽 서브트리의 모든 값은 현재 노드 값보다 큼.
            2. 초기값의 범위를 (-inf, inf)로 설정
            3. 각 노드의 값을 검사하고, 범위를 업데이트해서 재귀적으로 서브 트리 확인
        - Time Complexity: O(n). n은 트리의 노드 수
            모든 노드를 한번씩 방문한다.
        - Space Complexity: O(h). h는 트리의 높이
            재귀 호출 스택이 트리의 높이만큼 공간을 필요로 한다.
            편향된 트리라면 O(n)이 필요하다.
        """

        def isValid(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (node.val < high and node.val > low):
                return False

            return isValid(node.left, low, node.val) and isValid(
                node.right, node.val, high
            )

        return isValid(root, float("-inf"), float("inf"))
