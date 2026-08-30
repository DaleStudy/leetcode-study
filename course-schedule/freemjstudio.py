class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # cycle 을 감지하면 false 를 리턴한다.
        graph = [[] for _ in range(numCourses)]

        # a <- b
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses
        # 0: unvisited 1: visiting 2: done

        def dfs(node):
            if state[node] == 1:
                return False

            if state[node] == 2:
                return True

            state[node] = 1 # visiting

            for next_node in graph[node]:
                if dfs(next_node) == False:
                    return False

            state[node] = 2 # done
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return False

        return True
