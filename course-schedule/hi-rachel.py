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
