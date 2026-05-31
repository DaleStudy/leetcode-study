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
