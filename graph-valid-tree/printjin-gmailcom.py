class Solution:
    def valid_tree(self, n, edges):
        if len(edges) != n - 1:
            return False
        parent = [i for i in range(n)]
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            parent[pu] = pv
        return True
