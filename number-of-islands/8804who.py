class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        answer = 0
        moves = [[-1,0],[1,0],[0,1],[0,-1]]
        visited = [[False for _ in range(m)] for _ in range(n)]
        def dfs(y, x):
            for move in moves:
                moved_y, moved_x = y+move[0], x+move[1]
                if n > moved_y >= 0 and m > moved_x >= 0:
                    if grid[moved_y][moved_x] == '1' and not visited[moved_y][moved_x]:
                        visited[moved_y][moved_x] = True
                        dfs(moved_y, moved_x)
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == '1':
                    visited[i][j] = True
                    answer += 1
                    dfs(i, j)
        return answer
    
