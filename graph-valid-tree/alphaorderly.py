"""
시간복잡도: O(n)
공간복잡도: O(n)

먼저 트리의 조건에 맞도록 간선의 갯수가 노드의 갯수 - 1인지 확인하고
Union-Find 알고리즘을 사용하여 간선을 하나씩 추가하며 사이클 여부를 확인한다.
"""
class UnionFind:
    def __init__(self, n: int):
        self.parent = [-1] * n
        self.rank = [0] * n

    def find(self, target: int) -> int:
        if self.parent[target] == -1:
            return target

        self.parent[target] = self.find(self.parent[target])
        return self.parent[target]

    def union(self, a: int, b: int) -> bool:
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False

        if self.rank[a] < self.rank[b]:
            a, b = b, a

        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1

        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) < n - 1:
            return False

        u = UnionFind(n)

        for a, b in edges:
            if not u.union(a, b):
                return False

        return True
