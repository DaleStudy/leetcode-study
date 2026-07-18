# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 시간 복잡도: O(N), 모든 노드를 한번 씩 방문
# 공간 복잡도: O(N), 최악의 경우 모든 노드가 큐에 담길 수 있음
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_depth = 1
        stack = [(root, 1)]

        while stack:
            node, cur_depth = stack.pop()
            max_depth = max(cur_depth, max_depth)

            if node.left:
                stack.append((node.left, cur_depth + 1))

            if node.right:
                stack.append((node.right, cur_depth + 1))

        return max_depth
