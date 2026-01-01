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
        old_to_new = {}

        def dfs(curr_node):
            if curr_node in old_to_new:
                return old_to_new[curr_node]
            
            copy = Node(curr_node.val)
            old_to_new[curr_node] = copy

            for neighbors in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbors))

            return copy

        return dfs(node)
    
    # O(N+E) time complexity where N is the number of nodes and E is the number of edges in the graph.
    # O(N) space complexity for the hashmap and the recursion stack in the worst case.
    
    