from collections import deque
class Solution:
    # 시간복잡도: O(numCourses + prerequisites의 길이)
    # 공간복잡도: O(numCourses + prerequisites의 길이)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        reachable = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            reachable[a] += 1
            graph[b].append(a)

        q = deque()
        visited = set()
        for i in range(numCourses):
            if reachable[i] == 0:
                q.append(i)
                visited.add(i)

        while q:
            node = q.popleft()

            for next_node in graph[node]:
                reachable[next_node] -= 1
                if next_node not in visited and reachable[next_node] == 0:
                    q.append(next_node)
                    visited.add(next_node)

        if len(visited) == numCourses:
            return True

        return False
