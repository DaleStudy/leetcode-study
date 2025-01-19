class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
		# TC : O(n*m)
		# SC : O(n*m)

        m, n = len(grid), len(grid[0])
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        def in_range(r, c):
            if r<0 or c<0 or r>=m or c>=n:
                return False
            return True

        # DFS Way

        def dfs(r, c):
            grid[r][c] = 'x'

            for i in range(4):
                nr, nc = r+dx[i], c+dy[i]
                if not in_range(nr, nc) or grid[nr][nc] != '1':
                    continue
                dfs(nr, nc)
        
        # BFS Way
        from collections import deque
        def bfs(r, c):
            grid[r][c] = 'x'
            queue = deque()
            queue.append([r, c])

            while queue:
                cr, cc = queue.popleft()
                for i in range(4):
                    nr, nc = cr+dx[i], cc+dy[i]
                    
                    if not in_range(nr, nc) or grid[nr][nc] != '1':
                        continue
                    grid[nr][nc] = 'x'
                    queue.append([nr, nc])

        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    ret += 1
        return ret

