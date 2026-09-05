
"""
# 시간 복잡도: O(n) (Union Find 연산은 경로 압축과 rank 활용으로 Amortized O(1))
# 공간 복잡도: O(n)
#
# Union-Find(유니온 파인드, Disjoint Set Union) 알고리즘을 사용해 무방향 그래프의 연결 요소(connected components) 개수를 계산한다.
#
# 알고리즘 단계:
# 1. 각 노드는 자기 자신을 부모로 갖도록(parent 배열) 초기화한다.
# 2. 트리의 깊이(랭크, rank)를 저장하는 배열을 초기화한다.
# 3. 간선을 하나씩 확인하며 union 연산으로 두 노드를 같은 집합으로 합친다.
#    - 이미 같은 집합인 경우엔 아무 작업도 하지 않는다.
#    - 서로 다른 집합을 합치면, 연결 요소 개수를 1 감소시킨다.
# 4. 모든 간선을 처리하고 남은 연결 요소 개수(ans)를 반환한다.
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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        ans = n

        for a, b in edges:
            if uf.union(a, b):
                ans -= 1

        return ans
