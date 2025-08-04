"""
모든 왼쪽 서브트리는 현재 노드보다 작아야 하고,
모든 오른쪽 서브트리는 현재 노드보다 커야 한다.

이걸 위해서 범위(min/max)를 재귀로 내려보내야 한다.

TC: O(n), 모든 노드 1번씩 탐색
SC: O(h), 재귀 호출 스택, h는 트리 높이
"""

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True  # 비어있는 노드는 BST
            # 현재 노드가 범위 밖이면 BST 조건 위배
            if not (low < node.val < high):
                return False
            # 왼쪽은 최대값을 현재 노드보다 작게 제한
            # 오른쪽은 최소값을 현재 노드보다 크게 제한
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root, float('-inf'), float('inf'))


"""
스택 풀이

- BST에서 중위 순회하면 항상 오름차순이어야 한다는 성질을 이용한 방법
- 중위 순회: 왼쪽 → 현재 노드 → 오른쪽
- BST는 중위 순회 시 값이 항상 증가해야 하므로, (오름차순)
  이전 노드(prev)보다 현재 노드 값이 작거나 같으면 잘못된 BST

TC: O(n), 모든 노드 1번씩 탐색
SC: O(h), 최대 스택 깊이 = 트리 높이
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = None  # 이전 중위 순회 값

        while stack or root:
            # 왼쪽 끝까지 탐색
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            # 이전 값보다 작거나 같으면 BST 위반
            if prev is not None and root.val <= prev:
                return False
            prev = root.val

            # 오른쪽으로 이동
            root = root.right

        return True


# O(n) time, O(n) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 좌측 서브 트리로 내려갈 떄:
#     - 하한값: 부모 노드의 하한값
#     - 상한값: 부모 노드의 값
# 우측 서브 트리로 내려갈 때:
#     - 하한값: 부모 노드의 값
#     - 상한값: 부모 노드의 상한값

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float('-inf'), float("inf"))
