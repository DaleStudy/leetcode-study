class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # 재귀 DFS
        # 그래프 만들기
        # graph[i] = [j, ...] : i를 듣기 위해 선행해야 하는 과목j들 저장
        graph = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            graph[i].append(j)

        # visited
        # 0: 방문 안함
        # 1: 방문 중(현재 탐색 중)
        # 2: 방문 완료(사이클 없음 확인 완료)
        visited = [0]*numCourses
        
        def dfs(course):
            # 방문 중인데 또 방문 = 사이클 존재 -> False
            if visited[course] == 1:
                return False

            # 이미 방문 완료(탐색 완료)
            if visited[course] == 2:
                return True
            
            # 방문 중 표시
            visited[course] = 1

            # 선행과목들 DFS로 확인
            for i in graph[course]:
                if not dfs(i):
                    return False

            # 탐색 완료(방문 완료)
            visited[course] = 2

            return True

        # 모든 과목 DFS 탐색
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
