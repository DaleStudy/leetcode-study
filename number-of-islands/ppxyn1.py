#idea : bfs
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while q:
                row, col = q.popleft()
                for x, y in directions:
                    nr, nc = row + x, col + y
                    
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == "1" and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            q.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands


