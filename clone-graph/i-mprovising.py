"""
Time complexity O(V + E)
Space complexity O(V + E)

DFS, BFS
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 

        clones = {}

        def dfs(node):
            if node in clones:
                return clones[node]
            clone = Node(node.val)
            clones[node] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone

        return dfs(node)
    
    def bfs(self, node):
          if not node:
            return
          
        clone = Node(node.val)
        clones = {node: clone}
        queue = deque([node])
        while queue:
            node = queue.popleft()
            for nei in node.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val)
                    queue.append(nei)
                clones[node].neighbors.append(clones[nei])
        return clone