class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # DFS (시간복잡도 O(m*n), 공간복잡도 O(m*n))
        answer = 0  # 섬의 수
        m = len(grid)
        n = len(grid[0])

        # 하나의 섬 처리(연결된 땅 모두 방문)
        def dfs(x,y):
            # 범위를 벗어나거나, 이미 방문했거나, 땅이 아니면 종료
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != "1":
                return
            
            # 현재 땅 방문처리
            grid[x][y] = "*"

            # 상하좌우 탐색
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        for i in range(m):
            for j in range(n):
                # 땅 발견시 dfs로 연결되어 있는 모든 땅 방문하고 섬+1 처리
                if grid[i][j] == "1":
                    dfs(i,j)
                    answer += 1

        return answer
