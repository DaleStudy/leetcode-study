# https://leetcode.com/problems/course-schedule/

from typing import List

class Solution:
    def canFinish_topo(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        [Complexity]
            - TC: O(v + e) (v = numCourses, e = len(prerequisites))
            - SC: O(v + e) (graph)

        [Approach]
            course schedule은 directed graph이므로, topological sort(BFS)를 이용해 방문한 노드의 개수가 numCourses와 같은지 확인한다.
        """
        from collections import deque

        # directed graph
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)  # b -> a
            indegree[a] += 1

        def topo_sort():
            # topological sort로 방문한 course 개수
            cnt = 0

            # indegree가 0인 course 부터 시작
            q = deque([i for i in range(numCourses) if indegree[i] == 0])

            while q:
                pos = q.popleft()

                # 방문한 course 개수 세기
                cnt += 1

                for npos in graph[pos]:
                    # npos의 indegree 감소
                    indegree[npos] -= 1
                    # indegree[npos] == 0, 즉, npos를 방문하기 위한 prerequisite이 모두 방문되었다면, q에 npos 추가
                    if indegree[npos] == 0:
                        q.append(npos)

            return cnt

        return numCourses == topo_sort()

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        [Complexity]
            - TC: O(v + e) (모든 노드 & 간선은 한 번 씩 방문, 재귀 호출도 첫 방문 시에만 수행)
            - SC: O(v + e) (graph)

        [Approach]
            course schedule은 directed graph이므로, 모든 course를 끝낼 수 없다는 것은 directed graph에 cycle이 존재한다는 것이다.
            directed graph의 cycle 여부를 판단하기 위해 3-state DFS를 사용할 수 있다.
                1) 이전에 이미 방문한 상태 (visited)
                2) 현재 보고 있는 경로에 이미 존재하는 상태 (current_path) -> 재귀 실행 전에 추가 & 후에 제거
                3) 아직 방문하지 않은 상태
        """

        graph = [[] for _ in range(numCourses)]  # directed graph
        visited = set()  # 이전에 이미 방문한 노드 기록
        current_path = set()  # 현재 경로에 이미 존재하는 노드를 만났다면, cycle이 존재하는 것

        for a, b in prerequisites:
            graph[b].append(a)  # b -> a

        def is_cyclic(pos):
            # base condition
            # 1) pos가 current_path에 이미 존재한다면, cycle 발견
            if pos in current_path:
                return True
            # 2) pos가 이전에 이미 방문한 (+ cycle이 존재하지 않는 경로 위의) 노드라면, cycle 발견 X
            if pos in visited:
                return False

            # recur (backtracking)
            current_path.add(pos)  # 현재 경로에 추가
            for npos in graph[pos]:
                if is_cyclic(npos):
                    return True
            current_path.remove(pos)  # 현재 경로에서 제거

            # 방문 처리 (+ cycle이 존재하지 않는 경로 위에 있음을 표시)
            visited.add(pos)

            return False

        for i in range(numCourses):
            # course schedule에 cycle이 존재한다면, 전체 course를 완료할 수 없음
            if is_cyclic(i):
                return False

        return True
