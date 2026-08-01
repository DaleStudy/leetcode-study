# 우 -> 하 -> 좌 -> 상

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        rows, cols = len(matrix), len(matrix[0])

        visited = [[False] * cols for _ in range(rows)]

        answer = []

        def dfs(xx: int, yy:int, d:int):

            i = d
            cnt = 0
            while cnt <= 5:
                nx = xx + dx[i]
                ny = yy + dy[i]

                if 0 <= nx and nx < cols and 0 <= ny and ny < rows:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        answer.append(matrix[ny][nx])
                        dfs(nx,ny,i)
                        return
                if i == 3:
                    i = 0
                else:
                    i = i + 1
                cnt = cnt + 1
                
                        
        
        visited[0][0] = True
        answer.append(matrix[0][0])
        dfs(0,0,0)
                        
        return answer





# ---------



# 우 -> 하 -> 좌 -> 상 

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        answer = []

        dx = [1,0,-1,0]
        dy = [0,1,0,-1]

        row_len , col_len = len(matrix), len(matrix[0])
        visited = [[False] * col_len for _ in range(row_len)]

        xx = 0
        yy = 0
        answer.append(matrix[yy][xx])
        visited[yy][xx] = True

        if len(answer) == row_len * col_len:
            return answer

        d = 0
        while True:            
            nx = xx + dx[d]
            ny = yy + dy[d]
            if 0 <= nx and nx < col_len and 0 <= ny and ny < row_len:
                if not visited[ny][nx]:
                    answer.append(matrix[ny][nx])
                    visited[ny][nx] = True

                    if len(answer) == row_len * col_len:
                        break

                    xx = nx
                    yy = ny
                    continue
            d = 0 if d == 3 else d + 1
        
        return answer

