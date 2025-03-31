"""
    풀이 :
        valid tree를 만족하려면 두 가지 조건이 필요하다

            1. 순환이 없어야 한다
            2. 모든 노드가 연결되어 있어야한다
        
        이 조건을 만족하려면 (vertex 수 - 1) == edge 수 가 필수조건이다
        edge 수가 더 적다면 모든 노드가 연결되지 않고 더 많다면 필연적으로 순환이 존재하기 때문
        위 조건으로 필터링하고 나서 모든 노드가 연결됐는지지 확인하면 valid tree를 알 수 있다
        즉, 순환을 가지고 있는지 확인하는 과정이 생략된다

    - edges를 기반으로 graph를 만든다

    노드 개수: N, 간선 개수: E
    E == N - 1을 먼저 확인하기 때문에 E는 N에 비례한다
    따라서 N만 사용

    TC: O(N)
        모든 node에 대해 dfs호출, edges에 대한 순회도 node수에 비례

    SC: O(N)
        dfs 호출 스택 및 graph는 node 수에 비례
"""

from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if n - 1 != len(edges) :
            return False

        graph = [[] for _ in range(n)]
        for node, adjcent in edges:
            graph[node].append(adjcent)
            graph[adjcent].append(node)
        
        visited = set()

        def dfs(node):
            visited.add(node)
            for adj in graph[node]:
                if adj not in visited:
                    dfs(adj)
        
        dfs(0)

        return len(visited) == n
