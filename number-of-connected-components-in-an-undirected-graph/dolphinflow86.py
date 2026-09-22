# n is the number of nodes, and E is the number of edges.
# TC: O(V + E * alpha(V)) - near linear time with path compression Union-Find
# SC: O(V) - parent and rank arrays for Union-Find


class Solution:

    def countComponents(self, n: int, edges) -> int:
        parent = list(range(n))
        rank = [1] * n

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1

        components = n
        for u, v in edges:
            components -= union(u, v)

        return components
