from collections import deque 

#  Runtime: 241ms, Memory: 18.94MB
#  Time complexity: O(len(n*m))
#  Space complexity: O(len(n*m))


class Solution:
    def bfs(self, a,b, grid, visited) :
        n = len(grid)
        m = len(grid[0])

        dx = [0, 0, 1, -1]
        dy = [1, -1 ,0 ,0]
        q = deque()
        q.append([a,b])
        visited[a][b] = True

        while q :
            x,y = q.popleft()

            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nx  < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '1'):
                    visited[nx][ny] = True
                    q.append([nx,ny])



    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        answer = 0
        
        for i in range(n) :
            for j in range(m) :
                if grid[i][j] == '1' and not visited[i][j] :
                    self.bfs(i,j,grid,visited)
                    answer += 1

        return answer
