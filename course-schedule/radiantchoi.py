from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        posts = defaultdict(list)
        indegree = [0] * numCourses

        for prerequisite in prerequisites:
            posts[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        completed = 0
        q = deque(list(filter(lambda x: indegree[x] == 0, range(numCourses))))

        while q:
            current = q.popleft()
            completed += 1

            for post in posts[current]:
                indegree[post] -= 1

                if indegree[post] == 0:
                    q.append(post)

        return completed == numCourses
