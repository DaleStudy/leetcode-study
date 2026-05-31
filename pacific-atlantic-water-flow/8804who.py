from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        answer = []
        h, w = len(heights), len(heights[0])
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        visited1 = [[False for _ in range(w)] for _ in range(h)]
        visited2 = [[False for _ in range(w)] for _ in range(h)]

        q1 = deque()
        q2 = deque()

        for i in range(w):    
            q1.append((0, i))
            q2.append((h-1, i))
            visited1[0][i] = True
            visited2[h-1][i] = True

        for i in range(h):
            q1.append((i, 0))
            q2.append((i, w-1))
            visited1[i][0] = True
            visited2[i][w-1] = True

        while q1:
            y, x = q1.popleft()

            for move in moves:
                next_y, next_x = y+move[0], x+move[1]

                if 0 <= next_y < h and 0 <= next_x < w:
                    if visited1[next_y][next_x]:
                        continue
                    if heights[next_y][next_x] >= heights[y][x]:
                        visited1[next_y][next_x] = True
                        q1.append((next_y, next_x))

        while q2:
            y, x = q2.popleft()

            for move in moves:
                next_y, next_x = y+move[0], x+move[1]

                if 0 <= next_y < h and 0 <= next_x < w:
                    if visited2[next_y][next_x]:
                        continue
                    if heights[next_y][next_x] >= heights[y][x]:
                        visited2[next_y][next_x] = True
                        q2.append((next_y, next_x))

        for i in range(h):
            for j in range(w):
                if visited1[i][j] and visited2[i][j]:
                    answer.append([i, j])
        return answer
    
