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
        
        visited = {}
        
        def dfs(node: 'Node') -> 'Node':
            if node.val in visited:
                return visited[node.val]
            
            # 노드 복제
            cloned_node = Node(node.val)
            visited[node.val] = cloned_node

            # 이웃들 복제
            for neighbor in node.neighbors:
                cloned_neighbor = dfs(neighbor)
                cloned_node.neighbors.append(cloned_neighbor)
            
            return cloned_node
        
        return dfs(node)
