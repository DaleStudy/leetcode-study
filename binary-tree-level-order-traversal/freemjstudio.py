from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        visits = []

        # bfs
        queue = deque([])
        queue.append(root)

        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    temp.append(node.val)

                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
            if temp:
                visits.append(temp)

        return visits
