class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # *문제 이해에 시간이 많이 걸림.
        # 각 칸에서 시작한 물이 태평양과 대서양 두 바다 모두로 흘러갈 수 있는 칸들 찾는 문제(높이가 같거나 낮은쪽으로만 물이 이동 가능함)
        # 문제를 역으로 생각해서 바다에서 물이 올라갈 수 있는 칸(더 높거나 같은 칸) 찾기.
        # DFS(시간복잡도 O(m*n), 공간복잡도 O(m*n))

        m, n = len(heights), len(heights[0])
        pac = set()     # 태평양 갈 수 있는 칸 저장
        atl = set()     # 대서양 갈 수 있는 칸 저장
        directions = [(-1,0), (1,0), (0,-1), (0,1)]  # 상하좌우
        
        def dfs(x, y, visited):
            visited.add((x,y))  # 현재위치 방문처리

            # 현재 위치에서 상하좌우 탐색
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # 다음 위치가 범위안이고, 아직 방문하지 않았고, 물이 흘러갈 수 있는 높이라면, 탐색
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and heights[nx][ny] >= heights[x][y]:
                    dfs(nx, ny, visited)

        
        for i in range(m):
            dfs(i, 0, pac)      # 왼쪽(pacific)
            dfs(i, n-1, atl)    # 오른쪽(atlantic)
        for j in range(n):
            dfs(0, j, pac)      # 위쪽(pacific)
            dfs(m-1, j, atl)    # 아래쪽(atlantic)

        # 교집합(태평양,대서양 모두 갈 수 있는 좌표의 교집합)
        return list(pac & atl)
