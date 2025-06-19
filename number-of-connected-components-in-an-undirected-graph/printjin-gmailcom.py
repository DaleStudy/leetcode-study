from typing import (
    List,
)

class Solution:
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        for a, b in edges:
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                parent[root_a] = root_b
                n -= 1
        return n
