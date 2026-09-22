"""
시간 복잡도: O(N)
공간 복잡도: O(N)

이 코드는 이진 탐색 트리(BST)에서 k번째로 작은 값을 찾는 함수입니다.
중위 순회를 통해 노드를 오름차순으로 방문하여,
k번째 값을 찾는 방식으로 동작합니다.
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        index = 1

        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack.pop()

            if index == k:
                return node.val
            index += 1

            if not node.right:
                continue

            right = node.right
            while right:
                stack.append(right)
                right = right.left

        return -1
