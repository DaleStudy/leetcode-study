"""
[결과 요약]
# 시도한 로직 수: 1
    1. 위상 정렬로 푸는 방법
        - 시간복잡도 O(n) / 공간복잡도 O(n)
            - 실제로는 numCourses + len(prerequisites) 만큼의 복잡도
"""

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
            required_courses[current] = -1
            done += 1

            # 이 강의의 선행 강의 찾기
            for next_ in course_graph[current]:
                required_courses[next_] -= 1

                if required_courses[next_] == 0:
                    available_courses.append(next_)

        return True if done == numCourses else False


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
