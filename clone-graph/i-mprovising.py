"""
Time complexity O(V + E)
Space complexity O(V + E)

DFS, BFS
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # dfs
        if not node:
            return 

        clone = Node(node.val)
        graph = {node:clone}
        stack = [node]
        
        while stack:
            node = stack.pop()
            for n in node.neighbors:
                if n not in graph:
                    stack.append(n)
                    graph[n] = Node(n.val)
                graph[node].neighbors.append(graph[n])

        return clone
    
    def bfs(self, node):
        if not node:
            return
          
        clone = Node(node.val) # clone first node
        clones = {node: clone} # reference node : clone node
        queue = deque([node])
        while queue:
            node = queue.popleft()
            for nei in node.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val) # clone node
                    queue.append(nei) # append queue neighbor reference node
                clones[node].neighbors.append(clones[nei]) 
        return clone