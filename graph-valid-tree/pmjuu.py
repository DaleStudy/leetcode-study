'''
노드의 개수를 n, 간선의 개수를 e 라고 할때,

시간 복잡도: O(n + e)
- 그래프의 모든 노드와 간선을 방문하므로 O(n + e)

공간 복잡도: O(n + e)
- 인접 리스트와 방문 배열을 저장하는 데 O(n + e)의 공간이 필요합니다.
'''
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:        
        graph = { i: [] for i in range(n) }
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def hasCycle(node, parent):
            if node in visited:
                return True
            
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # 부모 노드로 돌아가지 않기
                if hasCycle(neighbor, node):
                    return True
            
            return False

        # 0번 노드에서 DFS 시작
        if hasCycle(0, -1):
            return False

        # 모든 노드가 방문되었는지 확인 (연결성 체크)
        return len(visited) == n

# Example
solution = Solution()
print(solution.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))  # Output: True
print(solution.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))  # Output: False
