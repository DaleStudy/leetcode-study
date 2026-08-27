# TC: O(N)
# SC: O(N)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereq_dict = defaultdict(set)
        in_deg = [0] * numCourses
        is_completed = set()

        for prereq in prerequisites:
            prereq_dict[prereq[1]].add(prereq[0])
            in_deg[prereq[0]] += 1

        while True:
            course_list = []

            for idx in range(numCourses):
                if idx not in is_completed and in_deg[idx] == 0:
                    course_list.append(idx)

            if len(course_list) == 0:
                break

            for course in course_list:
                is_completed.add(course)

                for nxt in prereq_dict[course]:
                    in_deg[nxt] -= 1

        for idx in range(numCourses):
            if idx not in is_completed:
                return False

        return True

