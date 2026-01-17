from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for start, end in prerequisites:
            pre[end]+=1
            graph[start].append(end)

        q = deque()

        for i in range(numCourses):
            if pre[i] == 0:
                q.append(i)

        while q:
            n = q.popleft()
            numCourses -= 1

            for post in graph[n]:
                pre[post] -= 1
                if pre[post] == 0:
                    q.append(post)
        
        return numCourses == 0
    
