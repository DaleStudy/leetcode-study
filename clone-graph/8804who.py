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
            return 
        visited = {}
        new_node = Node()
        def dfs(original_node, new_node):
            if original_node.val in visited:
                return
            visited[original_node.val] = new_node
            new_node.val = original_node.val
            new_node.neighbors = []

            for neighbor in original_node.neighbors:
                new_node.neighbors.append(Node())
                if neighbor.val not in visited:
                    dfs(neighbor, new_node.neighbors[-1])
                new_node.neighbors[-1] = visited[neighbor.val]
        dfs(node, new_node)
        return new_node
    


