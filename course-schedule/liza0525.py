from collections import defaultdict

# 7기 풀이
# 시간 복잡도: O(V + E)
# - numCourses(V)와 prerequisites의 길이(E)에 비례
# 공간 복잡도: O(V)
# - 각 과목의 상태를 계산하는 state와 prereq_map의 공간은 numCourses(V)에 비례

BEFORE_START = 0
IN_PROGRESS = 1
DONE = 2
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # states: 각 과목의 상태 저장, index가 곧 과목을 나타냄
        states = [BEFORE_START] * numCourses
        
        # 선수과목(key) 당 다음 과목들(value) 정보 저장
        prereq_map = defaultdict(list)

        for next_course, pre_course in prerequisites:
            prereq_map[pre_course].append(next_course)

        def dfs(course):
            if states[course] != BEFORE_START:
                # 이미 들었거나, 듣는 중이라면 더이상 탐색하지 않아도 됨
                return

            states[course] = IN_PROGRESS  # 현재 과목을 듣는 중 상태로 변경

            next_courses = prereq_map.get(course, [])  # 다음 과목의 정보 가져오기

            for next_course in next_courses:
                # 다음 과목들도 모두 돌아본다
                if states[next_course] == IN_PROGRESS:
                    # 다음 과목을 듣고 있는 중이라면, 서로가 선수과목이 된다는 이야기(그래프의 사이클이 생김)
                    # 이 때는 더이상 탐색하지 않고 return한다.
                    return
                # 다음 과목에 대한 탐색
                dfs(next_course)

            # 다음 과목들도 다 들었다고 하면 사이클이 없으므로 해당 과목도 들었음 상태로 변경
            states[course] = DONE
        

        for course in range(numCourses):
            dfs(course)

        return IN_PROGRESS not in states  # 듣는 중 상태의 존재 여부를 return
