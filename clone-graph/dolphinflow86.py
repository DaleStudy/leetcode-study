# N is the number of nodes, and E is the number of edges.
# TC: O(N + E) - visits each node and edge once
# SC: O(N) - uses a hash map for cloned nodes and the recursion stack

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
        if not node:
            return None

        cloned = {}

        def dfs(curr):
            if curr in cloned:
                return cloned[curr]

            copy = Node(curr.val)
            cloned[curr] = copy

            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
