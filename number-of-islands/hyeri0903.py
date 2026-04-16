class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        m = 세로(열), n = 가로(행)
        solution: dfs
        '''
        m = len(grid)
        n = len(grid[0])
        visited = [ [0] * n for _ in range(m)]
        count = 0

        def dfs(i, j):
            #범위 벗어나면 return
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return

            if visited[i][j] == 1:
                return

            visited[i][j] = 1 #방문표시

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    dfs(i,j)
                    count += 1
        return count
        
