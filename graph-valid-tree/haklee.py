"""
아이디어:
- 트리여야 하므로 엣지 개수가 n-1개여야 한다.
- 엣지 개수가 n-1개이므로 만약 중간에 사이클이 있다면 트리가 연결이 안 된다.
    - 연결이 안 되었으니 트리는 아니고... 몇 조각으로 쪼개진 그래프가 된다. 여튼, valid tree가
      아니게 된다.
    - spanning tree 만들 때를 생각해보자. 엣지 하나를 더할 때마다 노드가 하나씩 트리에 추가되어야
      엣지 n-1개로 노드 n개를 겨우 만들 수 있는데, 중간에 새로운 노드를 추가 안하고 엄한 곳에
      엣지를 써서 사이클을 만들거나 하면 모든 노드를 연결할 방법이 없다.
    - 위의 예시보다 좀 더 일반적으로는 union-find 알고리즘에서 설명하는 union 시행으로도 설명이
      가능하다. union-find에서는 처음에 n개의 노드들의 parent가 자기 자신으로 세팅되어 있는데,
      즉, 모든 노드들이 n개의 그룹으로 나뉘어있는데, 여기서 union을 한 번 시행할 때마다 그룹이 1개
      혹은 0개 줄어들 수 있다. 그런데 위 문제에서는 union을 엣지 개수 만큼, 즉, n-1회 시행할 수 있으므로,
      만약 union 시행에서 그룹의 개수가 줄어들지 않는 경우(즉, 엣지 연결을 통해 사이클이 생길 경우)가
      한 번이라도 발생하면 union 시행 후 그룹의 개수가 2 이상이 되어 노드들이 서로 연결되지 않아 트리를
      이루지 못한다.
"""

"""TC: O(n * α(n)), SC: O(n)

n은 주어진 노드의 개수, e는 주어진 엣지의 개수.

아이디어(이어서):
- union-find 아이디어를 그대로 활용한다.
    - 나이브한 접근:
        - union을 통해서 엣지로 연결된 두 집합을 합친다.
        - find를 통해서 0번째 노드와 모든 노드들이 같은 집합에 속해있는지 확인한다.
    - 더 좋은 구현:
        - union 시행 중 같은 집합에 속한 두 노드를 합치려고 하는 것을 발견하면 False 리턴
- union-find는 [Disjoint-set data structure - Wikipedia](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)
  를 기반으로 구현했다. 여기에 time complexity 관련 설명이 자세하게 나오는데 궁금하면 참고.

SC:
- union-find에서 쓸 parent 정보만 관리한다. 각 노드마다 parent 노드(인덱스), rank를 관리하므로 O(n).

TC:
- union 과정에 union by rank 적용시 O(α(n)) 만큼의 시간이 든다. 이때 α(n)은 inverse Ackermann function
  으로, 매우 느린 속도로 늘어나므로 사실상 상수라고 봐도 무방하다.
- union 시행을 최대 e번 진행하므로 O(e * α(n)).
- e = n-1 이므로 O(n * α(n)).
"""


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n, edges):
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
            # 원래는 값을 리턴하지 않아도 되지만, 같은 집합에 속한 노드를
            # union하려는 상황을 판별하기 위해 값 리턴.

            pa = find(a)
            pb = find(b)

            # union by rank
            if pa == pb:
                # parent가 같음. rank 작업 안 해도 된다.
                return True

            if rank[pa] < rank[pb]:
                pa, pb = pb, pa

            parent[pb] = pa

            if rank[pa] == rank[pb]:
                rank[pa] += 1

            return False

        if len(edges) != n - 1:
            # 트리에는 엣지가 `(노드 개수) - 1`개 만큼 있다.
            # 이 조건 만족 안하면 커팅.
            return False

        # 나이브한 구현:
        # - 모든 엣지로 union 시행
        # - find로 모든 노드가 0번 노드와 같은 집합에 속해있는지 확인

        # for e in edges:
        #     union(*e)

        # return all(find(0) == find(i) for i in range(n))

        # 더 좋은 구현:
        # - union 시행 중 같은 집합에 속한 두 노드를 합치려고 하는 것을 발견하면 False 리턴
        for e in edges:
            if union(*e):
                return False

        return True


"""TC: O(n), SC: O(n)

n은 주어진 노드의 개수, e는 주어진 엣지의 개수.

아이디어(이어서):
- 트리를 잘 이뤘는지 확인하려면 한 노드에서 시작해서 dfs를 돌려서 모든 노드들에 도달 가능한지
  체크하면 되는데, 이게 시간복잡도에 더 유리하지 않을까?

SC:
- adjacency list를 관리한다. O(e).
- 호출 스택은 탐색을 시작하는 노드로부터 사이클이 나오지 않는 경로의 최대 길이만큼 깊어질 수 있다.
  최악의 경우 O(n).
- 이때 e = n-1 이므로 종합하면 O(n).

TC:
- 각 노드에 접근하는 과정에 O(1). 이런 노드를 최악의 경우 n개 접근해야 하므로 O(n).
"""


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n, edges):
        # write your code here
        if len(edges) != n - 1:
            # 트리에는 엣지가 `(노드 개수) - 1`개 만큼 있다.
            # 이 조건 만족 안하면 커팅.
            return False

        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = [False for _ in range(n)]

        def dfs(node):
            visited[node] = True
            for adj in adj_list[node]:
                if not visited[adj]:
                    dfs(adj)

        # 한 노드에서 출발해서 모든 노드가 visted 되어야 주어진 엣지들로 트리를 만들 수 있다.
        # 아무 노드에서나 출발해도 되는데 0번째 노드를 선택하자.
        dfs(0)

        return all(visited)
