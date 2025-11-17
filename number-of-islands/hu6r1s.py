from collections import deque

class Solution:
    """
    문제를 보니 바로 그래프 탐색이 떠올라서 bfs 알고리즘을 사용해서 구현
    백준 문제에서 많이 풀어보던건데 너무 오래 되어 계속 헷갈렸음
    다시 공부해야함
    """
    def numIslands(self, grid: List[List[str]]) -> int:        
        def bfs(grid, i, j):
            queue = deque()
            queue.append([i, j])
            grid[i][j] = "0"
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if grid[nx][ny] == "0":
                        continue
                    grid[nx][ny] = "0"
                    queue.append([nx, ny])
            

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        n, m = len(grid), len(grid[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    bfs(grid, i, j)
                    cnt += 1
        return cnt
