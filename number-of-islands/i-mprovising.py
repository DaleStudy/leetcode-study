class Solution:
    """
    Time, Space comlexity O(n*m)
    
    connected components
    dfs, bfs
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)] # visited 대신 grid를 0으로 표시할수도 있다
        islands = 0
    
        def dfs(x, y):
            stack = [(x, y)]
            while stack:
                x, y = stack.pop()
                dx = [-1, 1, 0, 0]
                dy = [0, 0, -1, 1]
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0<=nx<=n-1 and 0<=ny<=m-1:
                        if not visited[nx][ny] and grid[nx][ny] == "1":
                            visited[nx][ny] = True
                            stack.append((nx, ny))

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1

        return islands
