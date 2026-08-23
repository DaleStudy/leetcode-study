from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        answer = []
        n, m = len(heights), len(heights[0])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def bfs(sx, sy):
            visited = set()
            visited_pacific = False
            visited_atlantic = False

            queue = deque([])
            queue.append((sx, sy)) # start position

            while queue:
                x, y = queue.popleft()
                # check if flows into pacific ocean
                if x <= 0:
                    visited_pacific = True

                # check if flows into atlantic ocean
                if x >= n:
                    visited_atlantic = True

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < m and not (nx, ny) in visited:
                        if heights[nx][ny] <= heights[x][y]:
                            queue.append((nx, ny))
                            visited.add((nx, ny))

            return visited_pacific and visited_atlantic


        for i in range(n):
            for j in range(m):
                if bfs(i, j):
                    answer.append([i, j])

        return answer
