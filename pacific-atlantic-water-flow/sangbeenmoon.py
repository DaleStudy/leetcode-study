class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m,n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        visited = [[False] * n for _ in range(m)]

        dx = [0,0,-1,1]
        dy = [-1,1,0,0]


        def go(root_x:int, root_y:int, xx:int, yy:int):

            for d in range(4):
                nx = xx + dx[d]
                ny = yy + dy[d]

                if ny == -1 or nx == -1:
                    pacific[root_y][root_x] = True
                if ny == m or nx == n:
                    atlantic[root_y][root_x] = True

                if 0 <= ny and ny < m and 0 <= nx and nx < n:
                    if heights[ny][nx] <= heights[yy][xx] and not visited[ny][nx]:
                        visited[ny][nx] = True
                        go(root_x, root_y, nx, ny)

        for y in range(m):
            for x in range(n):
                visited = [[False] * n for _ in range(m)]
                go(x,y,x,y)

        answer = []

        for y in range(m):
            for x in range(n):
                if pacific[y][x] and atlantic[y][x]:
                    answer.append([y,x])

        return answer
