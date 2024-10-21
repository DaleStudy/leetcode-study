from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    - Idea: 재귀를 이용하여 각 노드의 왼쪽 자식과 오른쪽 자식을 바꾼다.
    - Time Complexity: O(n). n은 전체 노드의 수다.
        모든 노드에 대해서 반복적으로 수행해야 하기 때문에 O(n) 시간이 걸린다.
    - Space Complexity: O(n). n은 전체 노드의 수다.
        최악의 경우, 불균형 트리에서는 재귀 호출로 인해 최대 O(n) 스택 공간이 필요하다.
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
