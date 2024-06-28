from collections import defaultdict


class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        visit = ["unvisited"] * numCourses

        def detectCycle(course):
            if visit[course] == "visiting":
                return True  # Cycle detected
            if visit[course] == "visited":
                return False  # Already fully visited

            visit[course] = "visiting"  # Mark as visiting

            for prerequisite in graph[course]:
                if detectCycle(prerequisite):
                    return True

            visit[course] = "visited"  # Mark as fully visited

            return False

        # Perform cycle detection for all courses
        for course in range(numCourses):
            if detectCycle(course):
                return False

        return True
