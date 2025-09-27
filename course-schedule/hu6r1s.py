from collections import defaultdict

class Solution:
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     for pre_x, pre_y in prerequisites:
    #         if [pre_y, pre_x] in prerequisites:
    #             return False
    #     return True


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)

        for x, y in prerequisites:
            d[x].append(y)
        
        visited = set()
        finished = set()

        def dfs(course):
            if course in visited:
                return False
            if course in finished:
                return True

            visited.add(course)
            for v in d[course]:
                if not dfs(v):
                    return False
            visited.remove(course)
            finished.add(course)
            return True

        for course in list(d):
            if not dfs(course):
                return False
        return True
