# 시간복잡도: O(N*M)
# 공간복잡도: O(N*M)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        n = len(matrix[0])
        m = len(matrix)
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        answer = []


        def dfs(x, y, direction):
            answer.append(matrix[x][y])
            nx = x + dx[direction]
            ny = y + dy[direction]


            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                return dfs(nx, ny, direction)

            direction = (direction+1) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                return dfs(nx, ny, direction)
            else:
                return answer

        return dfs(0, 0, 0)
