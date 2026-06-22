from typing import List
from collections import defaultdict, deque


# 7기 풀이
# 시간 복잡도: O(V + E)
# - 모든 노드과 연결된 엣지를 탐색하면서 component 개수를 확인하므로 노드 개수(V)와 엣지 개수(E)만큼 시간 소요
# 공간 복잡도: O(V + E)
# - 노드의 개수(V)와 엣지의 개수(E)만큼 mappers를 만드므로 V + E 만큼 공간 사용
class Solution:
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        mappers = defaultdict(list)

        for node1, node2 in edges:
            # 무방향 그래프의 정보 저장
            mappers[node1].append(node2)
            mappers[node2].append(node1)

        visited = [0 for _ in range(n)]

        def bfs(node):
            # bfs로 어떤 node들이 연결되어 있는 지 탐색한다.
            queue = deque([node])

            while queue:  # queue에 요소가 있는 동안은 계속 탐색
                node = queue.popleft()  # queue에서 가장 빠른 요소 pop
                visited[node] = 1  # 해당 노드는 방문 처리
                
                next_nodes = mappers.get(node, [])  # mappers에서 다음 노드 정보 가져오기
                for next_node in next_nodes:
                    if visited[next_node]:
                        # 다음 노드가 이미 방문한 노드라면 탐색하지 않고 스킵해도 됨
                        continue
                    # 다음 노드를 queue에 저장하여 다음 탐색 때 이용
                    queue.append((next_node))
            

        for node in range(n):
            if visited[node]:
                # 이미 방문 처리가 되었다면 해당 노드는 이전에 탐색 완료되었다는 의미
                # bfs 탐색의 시작점으로 사용하지 않고 skip한다
                continue

            # bfs 탐색
            bfs(node)

            # 탐색을 마쳤다면 component 하나를 찾았다는 의미로 res를 하나 올린다.
            res += 1

        return res
