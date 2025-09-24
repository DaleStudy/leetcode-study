"""
https://leetcode.com/problems/course-schedule/

문제: 수강 해야 하는 모든 강좌의 수 numCourses가 주어질 때, 모든 강좌를 끝낼 수 있으면 true, 아니면 false를 반환해라.
     prerequisites[i] = [ai, bi], bi를 수강하기 위해선 반드시 ai를 사전 수강해야만 한다.
     
풀이: 사이클이 있으면 수강 불가능 (순환 참조), 없으면 수강 가능
     각 강좌를 Node로 보고, 선행 과목 관계를 방향이 있는 간선(Edge)로 보면 -> 방향 그래프
     
     BFS 풀이
     1. 그래프 만들기
        graph[a] = [b, c] 이면 a를 듣기 전에 b, c를 들어야 한다.
        graph[b] = [a] 이면 b를 듣기 전에 a를 들어야 한다.

     2. 진입 차수 계산
        진입 차수: 어떤 노드로 들어오는 간선의 수
        진입 차수가 0인 노드는 바로 들을 수 있는 강의
     
     3. Queue에 진입 차수가 0인 노드부터 넣고 시작
        Queue에서 꺼낸 노드를 기준으로, 연결된 노드들의 진입차수를 하나씩 줄인다.
        진입차수가 0이 된 노드는 새로 Queue에 추가
     
     4, 처리된 노드 수가 전체 강의 수와 같으면 True, 아니면 False

TC: O(V + E), V: 과목 수, E: prerequisite 관계 수
SC: O(V + E), 그래프 + 진입차수 배열
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # 1. 그래프 만들기, 2. 진입차수 계산
        # 수강 강의, 사전 강의
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # 3. Queue에 진입 차수가 0인 노드부터 넣고 시작
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        completed = 0

        # 4. BFS 탐색, 처리된 노드 수가 전체 강의 수와 같으면 True, 아니면 False
        while queue:
            # queue에서 꺼낸 과목을 수강 완료 처리
            current = queue.popleft()
            completed += 1

            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            
        return completed == numCourses

"""
위상 정렬을 구하는 알고리즘
1. DFS 기반 (스택을 쌓아 뒤집는 방식)
2. Kahn 알고리즘 (진입차수 0부터 차례로 큐 처리)

Kahn 알고리즘이란?
방향 그래프에서 진입차수(indegree)가 0인 정점부터 차례로 제거(큐에 넣어 꺼내기)하며 위상 순서를 만드는 방법.
진입차수가 0인 정점이 하나도 없는데 아직 남은 정점이 있다면 사이클 존재 -> 위상 정렬 불가.

위상 순서: 방향 그래프에서 간선(u→v)이 있다면, 순서에서 u가 항상 v보다 앞에 나오는 정점들의 나열.
진입차수: 정점으로 들어오는 간선의 개수.


TC: O(V + E), V: 과목 수, E: prerequisite 관계 수
SC: O(V + E), 그래프 + 진입차수 배열
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
         # 1) 그래프(인접 리스트)와 진입차수 배열 만들기
        adj = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites:  # b -> a (b를 먼저 들어야 a를 들을 수 있음)
            adj[b].append(a)
            indeg[a] += 1
        
        # 2) 진입차수 0인 정점들로 큐 초기화
        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        taken = 0  # 처리(수강) 완료한 과목 수

        # 3) 큐에서 빼며 간선 제거(=후속 과목 진입차수 감소)
        while q:
            u = q.popleft()
            taken += 1
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        # 4) 모두 처리됐으면 사이클 없음
        return taken == numCourses


"""
DFS 기반
TC: O(V + E), V: 과목 수, E: prerequisite 관계 수
SC: O(V + E), 그래프 + 탐색 중인 과목 집합 + 수강 완료한 과목 집합
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            # 선수 과목을 원소로 추가
            graph[crs].append(pre)

        # 탐색중
        traversing = set()
        # 수강가능한 과목
        finished = set()

        def can_finish(crs):
            if crs in traversing:
                return False
            if crs in finished:
                return True
            
            traversing.add(crs)
            for pre in graph[crs]:
                if not can_finish(pre):
                    return False
            traversing.remove(crs)
            finished.add(crs)
            return True

        for crs in graph:
            if not can_finish(crs):
                return False
        return True

# 줄인 코드
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        traversing = set()

        @cache
        def can_finish(crs):
            if crs in traversing:
                return False
            
            traversing.add(crs)
            result = all(can_finish(pre) for pre in graph[crs])
            traversing.remove(crs)
            return result

        return all(can_finish(crs) for crs in graph)
