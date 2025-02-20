# Time Complexity: O(N) - iterate through all edges and nodes at most once.
# Space Complexity: O(N) - store the graph as an adjacency list and track visited nodes.

class Solution:    
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # a tree with 'n' nodes must have exactly 'n-1' edges
        if len(edges) != n - 1:
            return False

        # build an adjacency list (graph representation)
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # use BFS to check if the graph is fully connected and acyclic
        visited = set()
        queue = [0]
        visited.add(0)

        while queue:
            node = queue.pop(0)  
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)

        # if we visited all nodes, it's a valid tree
        return len(visited) == n
