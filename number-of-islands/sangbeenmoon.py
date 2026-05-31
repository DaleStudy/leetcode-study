class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m,n = len(grid[0]), len(grid)

        visited = [[False] * m for _ in range(n)]

        dx = [0,0, -1, 1]
        dy = [-1,1,0,0]

        def dfs(xx:int, yy:int):

            for d in range(4):
                nx = xx + dx[d]
                ny = yy + dy[d]

                if 0 <= nx and nx < m and 0 <= ny and ny < n and grid[ny][nx] == "1":
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        dfs(nx, ny)
        
        answer = 0

        for y in range(n):
            for x in range(m):
                if grid[y][x] == "1" and not visited[y][x]:
                    answer = answer + 1
                    dfs(x,y)
        return answer
