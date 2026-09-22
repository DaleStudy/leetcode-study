class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph
        edge = {}
        for dst, src in prerequisites:
            nodes = edge.get(dst, [])
            nodes.append(src)
            edge[dst] = nodes

        seen = set()
        def dfs(i):
            if i in seen:
                return False
            if i not in edge or edge[i] == []:
                return True
            seen.add(i)
            for pre in edge[i]:
                if not dfs(pre):
                    return False
            seen.remove(i)
            edge[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
