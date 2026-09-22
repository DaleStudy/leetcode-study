# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
시간복잡도: O(n)
공간복잡도: O(h) - 트리의 높이(h)만큼 재귀 호출이 쌓인다.

- 루트 노드부터 시작해, 왼쪽과 오른쪽 자식을 각각 재귀적으로 반전한다.
- 재귀 함수는 현재 노드가 None이면 바로 None을 반환한다.
- 왼쪽과 오른쪽 자식을 반전한 결과를 각각 root.right, root.left로 할당하여 두 자식을 서로 바꾼다.
- 최종적으로 반전된 루트 노드를 반환한다.
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
