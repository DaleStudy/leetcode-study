from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        - Idea: 각 과목의 선행 과목에 사이클이 존재하는지 DFS로 탐색한다.
            하나라도 사이클이 존재한다면, 모든 과목을 수강할 수 없다는 의미다.
        - Time Complexity: O(v + e). v와 e는 각각 과목의 수, e는 선행 관계(과목 => 선행 과목)의 수다.
            모든 과목과 그 과목의 선행 과목을 탐색해야 하기 때문에 각 노드와 엣지에 대해 한번씩 방문해야 한다.
        - Space Complexity: O(v). v는 과목의 수다.
            각 과목에 대해서 그래프(선행 관계)를 저장하고, 재귀 호출 스택에 의해 공간이 사용된다.
        """

        graph = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        visited = set()

        def DFS(course):
            if course in visited:
                return False
            if graph[course] == []:
                return True

            visited.add(course)
            for prerequisite in graph[course]:
                if not DFS(prerequisite):
                    return False

            visited.remove(course)
            graph[course] = []

            return True

        for course in range(numCourses):
            if not DFS(course):
                return False

        return True
