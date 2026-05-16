from collections import defaultdict

# 7기 풀이
# 시간 복잡도: O(V + E)
# - 노드 개수(V) 및 엣지의 개수(E)만큼 탐색하므로 이에 따라 시간이 걸림
# 공간 복잡도: O(V + E)
# - visited 노드의 개수(V)만큼, node_map는 엣지의 개수(E)만큼 생성함
# - 재귀 스택은 최대 V만큼 생김
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = [0 for _ in range(n)]
        node_map = defaultdict(list)  # 노드 연결 정보 저장할 mapper

        for node1, node2 in edges:
            # 각 엣지는 방향이 없으므로 양방향 정보 저장
            node_map[node1].append(node2)
            node_map[node2].append(node1)

        def check_is_not_cycle(prev_node, node):        
            if visited[node]:
                # node를 이미 방문했다면 cycle이 있다는 의미이므로 tree가 아님
                # False를 return한다
                return False

            visited[node] = 1  # 현재 노드 방문 확인

            next_nodes = node_map[node]
            if not next_nodes:
                # 더이상 방문할 것이 없다는 의미로
                # 해당 탐색은 cycle 없이 끝났다는 것을 의미
                return True

            for next_node in next_nodes:
                if prev_node == next_node:
                    # 양방향 노드 특성 상 prev_node 노드가 다음 노드와 같을 수 있다
                    # 이 때는 체크하지 않고 넘어간다
                    continue

                if not check_is_not_cycle(node, next_node):
                    # 재귀 함수의 결과가 False이면 False로 전파
                    return False

            # 함수 내의 모든 로직의 실행이 끝났다면 싸이클이 없다는 의미이므로
            # True를 return
            return True

        is_not_cycle = check_is_not_cycle(None, 0)

        # 싸이클이 없더라도 연결이 되지 않은 노드는 방문을 하지 않을 수 있기 때문에
        # visited에 0이 있는지 같이 확인하여 valid tree 여부를 return
        return 0 not in visited if is_not_cycle else False
