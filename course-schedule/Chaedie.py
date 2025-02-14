"""
(해설을 보면서 따라 풀었습니다.)

Solution: graph 에서 circular 가 생기면 false, 아니면 true

n: numCourses
p: number of preRequisites
Time: O(n + p) 
Space: O(n + p)
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        traversing = set()
        finished = set()

        def dfs(crs):
            if crs in traversing:
                return False
            if crs in finished:
                return True

            traversing.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            traversing.remove(crs)
            finished.add(crs)
            return True

        for crs in graph:
            if not dfs(crs):
                return False
        return True
