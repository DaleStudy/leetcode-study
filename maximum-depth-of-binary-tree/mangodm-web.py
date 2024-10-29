from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        - Idea: 이진 트리의 최대 깊이는 현재 노드의 깊이(1)와 하위 트리의 최대 깊이 중 큰 값을 더한 것으로 정의한다.
        - Time Complexity: O(n). n은 전체 노드의 수
            모든 노드를 한번씩 방문하여 탐색하기 때문에 O(n)이 소요된다.
        - Space Complexity: O(n). n은 전체 노드의 수
            재귀적으로 탐색할 때, 호출 스택에 쌓이는 함수 호출의 수는 최대 트리의 깊이와 같다.
            트리가 편향되어 있는 최악의 경우, 깊이가 n이 될 수 있기 때문에 O(n)으로 표현할 수 있다.
        """
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
