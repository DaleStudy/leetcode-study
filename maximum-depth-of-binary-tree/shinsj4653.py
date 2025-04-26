"""
[문제풀이]
# Inputs
- 이진 트리의 root
# Outputs
- 가장 최고 깊이
# Constraints
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
# Ideas
dfs, 즉 재귀 돌면서
depth 를 max로 업데이트 하면 될 것 같은 느낌?

[회고]
내 풀이는 정답
해설 방법도 궁금하여 참고
-> TC, SC도 파악하는 연습!

TC: o(n)
SC: o(n)

"""

# 내 풀이
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if node is None:
                return depth - 1

            return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))

        return dfs(root, 1)
# 해설
# bfs 풀이도 존재
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            max_depth = max(depth, max_depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return max_depth

