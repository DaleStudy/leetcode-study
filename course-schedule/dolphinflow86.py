# V is the number of numCourses, and E is the number of prerequisites.
# TC: O(V + E) - processes all vertices and edges in topological order
# SC: O(V + E) - stores graph adjacency list and indegree counts

from collections import deque


class Solution:

    def canFinish(self, numCourses: int, prerequisites) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for dest, src in prerequisites:
            adj[src].append(dest)
            indegrees[dest] += 1

        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        visited_count = 0

        while queue:
            node = queue.popleft()
            visited_count += 1

            for neighbor in adj[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        return visited_count == numCourses
