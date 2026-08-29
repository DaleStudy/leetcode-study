class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 -> 아직 미방문. 1 -> 방문중. 2 -> 방문 완료 && 사이클 없음.
        visited = [0] * numCourses
        graph = [[] for _ in range(numCourses)] 

        for prereq in prerequisites:
            src, dest = prereq[0], prereq[1]
            graph[src].append(dest)
        
        def go(cur: int) -> bool:
            visited[cur] = 1
            for next in graph[cur]:
                if visited[next] == 1:
                    return True
                if visited[next] == 0 and go(next):
                    return True

            visited[cur] = 2
            return False

        for cur in range(numCourses):
            if go(cur):
                return False

        return True
