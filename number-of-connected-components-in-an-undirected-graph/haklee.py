"""TC: O(n), SC: O(1)

n은 주어진 노드의 개수, e는 주어진 엣지의 개수.

아이디어:
- union-find를 활용하여 disjoint set을 찾는다.

SC:
- parent, rank값 관리에 각각 길이 n짜리 리스트가 필요하다. O(n).
- 결과 값을 찾을때 각 인덱스마다 find 함수의 결과를 찾아서 리스트로 만들고, 이를 set으로 만들어서
  길이 측정. 여기서도 O(n).
- 종합하면 O(n).

TC:
- union, find 각각 union by rank 적용시 O(α(n)) 만큼의 시간이 든다. 이때 α(n)은 inverse Ackermann function
  으로, 매우 느린 속도로 늘어나므로 사실상 상수라고 봐도 무방하다.
- union을 e회, find를 n회 시행하므로 O((n + e) * α(n)).
- 모든 노드에 find를 시행해서 얻은 값을 set으로 만들때 리스트를 전부 순회하므로 O(n).
- 종합하면 O((n + e) * α(n)).
"""


class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """

    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # write your code here

        # union find
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> bool:
            if x == parent[x]:
                return x

            parent[x] = find(parent[x])  # path-compression
            return parent[x]

        def union(a: int, b: int) -> bool:
            pa = find(a)
            pb = find(b)

            # union by rank
            if pa == pb:
                return

            if rank[pa] < rank[pb]:
                pa, pb = pb, pa

            parent[pb] = pa

            if rank[pa] == rank[pb]:
                rank[pa] += 1

        for e in edges:
            union(*e)

        return len(set(find(i) for i in range(n)))
