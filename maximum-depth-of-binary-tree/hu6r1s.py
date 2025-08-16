from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def bfs(n):
            queue = deque([n])
            depth = 0

            while queue:
                depth += 1
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return depth

        def dfs(n):
            stack = [n]
            max_depth = 0
            visited = {n: 1}

            while stack:
                node = stack.pop()
                depth = visited[node]
                max_depth = max(max_depth, depth)
                if node.left:
                    visited[node.left] = depth + 1
                    stack.append(node.left)
                if node.right:
                    visited[node.right] = depth + 1
                    stack.append(node.right)
            return max_depth
        
        return dfs(root)


"""
bfs 방식으로 left나 right가 있으면 스택에 넣고 depth + 1, dfs보다 비효율인 듯
"""
