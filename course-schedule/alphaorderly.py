
"""
시간복잡도: O(n + m)
공간복잡도: O(n + m)

- 각 과목의 진입 차수(in_degree)를 계산한다.
- 각 과목의 인접 리스트(graph)를 구성한다.
- 진입 차수가 0인 과목을 큐에 추가한다.
- 큐에서 과목을 하나씩 꺼내고, 그 과목을 선수과목으로 가지는 모든 과목의 진입 차수를 1씩 감소시킨다.
- 진입 차수가 0이 된 과목을 큐에 추가한다.
- 큐를 모두 처리한 후, 방문한 과목의 수가 전체 과목 수와 같은지 확인한다.
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = defaultdict(list)
        entered_courses = 0

        for s, e in prerequisites:
            in_degree[s] += 1
            graph[e].append(s)

        queue = deque([])

        for course, count in enumerate(in_degree):
            if count == 0:
                queue.append(course)
                entered_courses += 1

        while queue:
            course = queue.popleft()

            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    entered_courses += 1
                    queue.append(next_course)

        return entered_courses == numCourses
