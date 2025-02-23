'''
# 261. Graph Valid Tree

## What constitutes a 🌲
1. it's a graph.
2. Connected: edges == n - 1, visited node count == n
3. Acyclic: there is no cycle.

## Approach A. DFS
use DFS to check if there is a cycle in the graph.
- if there were no cycle & visited node count == n, return True.

## Approach B. Disjoint Set Union (서로소 집합)
use Disjoint Set Union to check if there is a cycle in the graph.
- if you find a cycle, return False immediately.
- if you find no cycle, return True.

### Union Find Operation
- Find: find the root of a node.
  - if the root of two nodes is already the same, there is a cycle.
- Union: connect two nodes. 

## Approach Comparison
- **A. DFS**: simple and easy to understand.
- **B. Disjoint Set Union**: quicker to check if there is a cycle. if there were more edges, Union Find would be faster.
'''
class Solution:
    def validTreeDFS(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = [[] for _ in range(n)]
        for node, neighbor in edges:
            graph[node].append(neighbor)
            graph[neighbor].append(node)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(0)
        return len(visited) == n
    
    def validTreeUnionFind(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parent = [i for i in range(n)]

        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        for node, neighbor in edges:
            if find(node) == find(neighbor):
                return False
            union(node, neighbor)

        return True
