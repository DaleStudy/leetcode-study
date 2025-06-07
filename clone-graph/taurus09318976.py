"""
문제의 핵심 포인트:
각 노드는 값과 이웃 노드들의 리스트를 가짐
원본 그래프와 완전히 독립적인 새로운 그래프 생성
모든 연결 관계를 그대로 복사

해결 방법:
DFS(깊이 우선 탐색) + 해시맵을 사용함:
해시맵으로 원본 노드와 복사본 노드의 매핑 관계 저장
DFS로 그래프를 순회하면서 각 노드를 복사
이미 복사된 노드는 해시맵에서 찾아서 재사용

Example 1의 경우
1 --- 2
|     |
|     |
4 --- 3

실행 과정:
노드 1 복사: clone_1 생성, visited = clone_1
노드 1의 이웃 2 복사: clone_2 생성, visited = clone_2
노드 2의 이웃 1 처리: 이미 visited에 있으므로 clone_1 반환
노드 2의 이웃 3 복사: clone_3 생성, visited = clone_3
노드 3의 이웃들 처리: clone_2, clone_4 연결
노드 1의 이웃 4 복사: clone_4 생성, visited = clone_4
모든 연결 관계 완성
Output: 원본과 동일한 구조의 완전히 새로운 그래프

시간 복잡도: O(V + E)
V: 노드(정점)의 개수, E: 간선의 개수
각 노드를 한 번씩 방문하고, 각 간선을 한 번씩 처리
DFS의 표준 시간 복잡도

공간 복잡도: O(V)
visited 해시맵이 모든 노드를 저장: O(V)
DFS 재귀 호출 스택의 최대 깊이: O(V)
복사된 그래프 자체도 O(V + E)의 공간 필요
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # 빈 그래프인 경우 None 반환
        if not node:
            return None
        
        # 원본 노드를 키로, 복사본 노드를 값으로 하는 해시맵 생성
        # 중복 복사를 방지하고 순환 참조 문제 해결
        visited = {}
        
        # DFS 함수 정의
        def dfs(original_node):
            # 이미 복사된 노드라면 기존 복사본을 반환 (중복 복사 방지)
            if original_node in visited:
                return visited[original_node]
            
            # 원본 노드의 값으로 새로운 노드 생성
            # 이웃 리스트는 빈 리스트로 초기화
            clone_node = Node(original_node.val, [])
            
            # 해시맵에 원본-복사본 매핑 관계 저장
            # 순환 참조 방지를 위해 이웃을 처리하기 전에 먼저 저장
            visited[original_node] = clone_node
            
            # 원본 노드의 모든 이웃들을 재귀적으로 복사
            # 복사된 이웃 노드들을 현재 복사본의 이웃 리스트에 추가
            for neighbor in original_node.neighbors:
                # 이웃 노드를 복사하고 현재 노드의 이웃 리스트에 추가
                clone_node.neighbors.append(dfs(neighbor))
            
            # 완성된 복사본 노드 반환
            return clone_node
        
        # 주어진 노드부터 DFS 시작
        return dfs(node)




