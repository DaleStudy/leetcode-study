"""
[결과 요약]
# 시도한 로직 수: 2
    1. 위상 정렬로 푸는 방법
        - 시간복잡도 O(n) / 공간복잡도 O(n)
            - 실제로는 numCourses + len(prerequisites) 만큼의 복잡도 (O(V+E))
        - 원리: 모든 노드를 정렬할 수 있는지 체크(순환이 있으면 모든 노드 정렬 불가)
    2. DFS를 활용하는 방법
        - 1번과 동일하게 O(V+E)
        - 원리: 탐색(비순환일때만 가능)을 완료할 수 있는지 체크해서 순환 여부를 판단

"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 3. DFS 함수 정의
        def dfs(current: int) -> bool:
            match course_states[current]:
                case 2:  # 탐색 완료
                    return True
                case 1:  # 탐색 중
                    return False
                case 0:  # 탐색 전
                    course_states[current] = 1
                    for next_ in course_graph[current]:
                        if not dfs(next_):
                            return False

                    course_states[current] = 2
                    return True

        # 1. 인덱스가 0부터 시작하는 그래프 초기화
        course_graph: list[list[int]] = [[] for _ in range(numCourses)]
        for after, before in prerequisites:
            course_graph[before].append(after)

        # 2. 각 노드별 탐색 상태를 표시하는 객체
        course_states: list[int] = [0] * numCourses

        # 3. 모든 노드를 1회씩 순회하면서 dfs
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


"""
# 위상정렬
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 1-a. 인덱스가 0부터 시작하는 그래프 초기화
        course_graph: list[list[int]] = [[] for _ in range(numCourses)]

        # 1-b. 각 노드별 선행 조건 갯수 리스트
        required_courses: list[int] = [0] * numCourses

        # 2. 선수과목을 돌면서 그래프를 채우기
        # Prerequisite이 [A, B]이면 A(After)를 수강하기 전에 B(Before)가 필요
        for after, before in prerequisites:
            course_graph[before].append(after)
            required_courses[after] += 1

        # 3. 현재 수강 가능한 강의 체크
        available_courses = deque()
        for i in range(numCourses):
            if required_courses[i] == 0:
                available_courses.append(i)

        # 4. queue가 빌 때까지
        done = 0
        while available_courses:

            # 수강 가능한 강의를 하나 꺼내서 수강 처리
            current = available_courses.popleft()
            done += 1

            # 이 강의의 선행 강의 찾기
            for next_ in course_graph[current]:
                required_courses[next_] -= 1

                if required_courses[next_] == 0:
                    available_courses.append(next_)

        return done == numCourses
"""


if __name__ == "__main__":

    test_cases = [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (3, [], True),
        (4, [[1, 0], [2, 1], [3, 2]], True),
        (5, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]], True),
        (1, [[0, 0]], False),
        (4, [[1, 0], [2, 1], [3, 2], [1, 3]], False),
    ]

    solution = Solution()

    for idx, (numCourses, prerequisites, expected) in enumerate(test_cases, start=1):

        result = solution.canFinish(numCourses, prerequisites)

        assert (
            result == expected
        ), f"Test Case {idx} Failed: Expected {expected}, Got {result}"

    print("All test cases passed.")
