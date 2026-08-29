# TC: O(V + E)
# SC: O(V + E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]
        in_deg = [0] * numCourses

        for nxt, prev in prerequisites:
            graph[prev].append(nxt)
            in_deg[nxt] += 1

        queue = deque(idx for idx in range(numCourses) if in_deg[idx] == 0)
        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1

            for nxt in graph[course]:
                in_deg[nxt] -= 1
                if in_deg[nxt] == 0:
                    queue.append(nxt)

        return completed == numCourses

