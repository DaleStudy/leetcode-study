"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = {}

        def deep_copy(node):
            if node is None:
                return None

            cur = Node(node.val)
            visited[node.val] = cur

            cur.val = node.val
            for neighbor in node.neighbors:
                if neighbor.val in visited:
                    cur.neighbors.append(visited[neighbor.val])
                else:
                    cur.neighbors.append(deep_copy(neighbor))

            return cur

        return deep_copy(node)
