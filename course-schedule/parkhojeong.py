class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_to_precourses: dict[str, set[int]] = {}
        precourse_to_courses: dict[str, set[int]] = {}

        for course, pre_course in prerequisites:
            if course not in course_to_precourses:
                course_to_precourses[course] = set()
            course_to_precourses[course].add(pre_course)

            if pre_course not in precourse_to_courses:
                precourse_to_courses[pre_course] = set()
            precourse_to_courses[pre_course].add(course)

        stack = []
        for course in range(numCourses):
            if course not in course_to_precourses:
                stack.append(course)

        while stack:
            pre_course = stack.pop()
            if pre_course in precourse_to_courses:
                for course in precourse_to_courses[pre_course]:
                    course_to_precourses[course].remove(pre_course)

                    if len(course_to_precourses[course]) == 0:
                        stack.append(course)

        for course in course_to_precourses:
            if len(course_to_precourses[course]) != 0:
                return False

        return True
