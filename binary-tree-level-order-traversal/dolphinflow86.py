# N is the total number of nodes in the binary tree.
# TC: O(N) - each node is visited and enqueued/dequeued once
# SC: O(N) - queue stores at most the maximum width of the tree (up to N / 2 nodes)

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def levelOrder(self, root: Optional["TreeNode"]) -> List[List[int]]:
        if not root:
            return []

        levels = []
        queue = deque([root])

        while queue:
            level_vals = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level_vals)

        return levels
