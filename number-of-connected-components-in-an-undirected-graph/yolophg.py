# Time Complexity: O(N + E) - go through all nodes & edges.
# Space Complexity: O(N) - store parent info for each node.

class Solution:
    def count_components(self, n: int, edges: List[List[int]]) -> int:

        # set up the Union-Find structure
        parent = [i for i in range(n)]  # initially, each node is its own parent
        rank = [1] * n  # used for optimization in Union operation

        # find function (with path compression)
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])  # path compression
            return parent[node]

        # union function (using rank to keep tree flat)
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1
                return True  # union was successful (i.e., we merged two components)
            return False  # already in the same component

        # connect nodes using Union-Find
        for a, b in edges:
            union(a, b)

        # count unique roots (number of connected components)
        return len(set(find(i) for i in range(n)))
