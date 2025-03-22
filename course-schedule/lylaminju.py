'''
시간 복잡도: O(V + E)
- 위상 정렬(Topological Sort)을 사용하여 모든 노드(과목)와 간선(선수 과목 관계)을 탐색하므로 O(V + E)입니다.
  - V: 노드(과목) 개수 (numCourses)
  - E: 간선(선수 과목 관계) 개수 (prerequisites의 길이)

공간 복잡도: O(V + E)
- 그래프를 인접 리스트로 저장하는 데 O(V + E) 공간이 필요합니다.
- 추가적으로 방문 상태를 저장하는 리스트가 필요하여 O(V).
- 따라서 총 공간 복잡도는 O(V + E)입니다.
'''

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프 초기화
        graph = {i: [] for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}

        # 선수 과목 정보 그래프에 저장
        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1

        # 진입 차수가 0인 과목(선수 과목이 없는 과목)을 큐에 추가
        queue = deque([course for course in in_degree if in_degree[course] == 0])
        completed_courses = 0

        while queue:
            current = queue.popleft()
            completed_courses += 1

            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # 모든 과목을 수강할 수 있다면 True, 아니면 False
        return completed_courses == numCourses
