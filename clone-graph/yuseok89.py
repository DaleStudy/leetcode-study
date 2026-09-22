# TC: O(N)
# SC: O(N)
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

        def rec(node: Optional['Node']) -> Optional['Node']:

            if not node:
                return None

            if node.val in visited:
                return visited[node.val]

            return_val = Node(node.val)
            visited[node.val] = return_val

            for neighbor in node.neighbors:
                cloned = rec(neighbor)

                if cloned:
                    return_val.neighbors.append(cloned)

            return return_val

        return rec(node)

