"""
# Intuition
트리 전체 순회

# Approach
-

# Complexity
time : O(N)
space : O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Stack (top-down)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # edge case
        if not root:
            return 0

        max_depth = 0
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()

            max_depth = max(depth, max_depth)  # update depth

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return max_depth


""" 재귀 (bottom-top)
# max_depth : 현재 노드를 기준으로, 좌측과 우측 자식 트리 중 max_depth가 큰 값을 선택해 + 1

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # 기저조건
        if not root:
            return 0

        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right),
        )
"""
