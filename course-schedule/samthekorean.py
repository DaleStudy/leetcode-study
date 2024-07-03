# V is number of verticles and E is number of edges
# TC : O(V+E)
# SC : O(V+E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre = defaultdict(list)

        for course, p in prerequisites:
            pre[course].append(p)

        taken = set()

        def dfs(course):
            if not pre[course]:
                return True

            if course in taken:
                return False

            taken.add(course)

            for p in pre[course]:
                if not dfs(p):
                    return False

            pre[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
