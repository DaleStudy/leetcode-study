# 시간복잡도: O(N*M*4^limit) limit: word의 길이
# 공간복잡도: O(N)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        limit = len(word)
        visited = [[False for _ in range(n)] for _ in range(m)]
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        target = 0

        def dfs(x, y, idx):

            if idx == limit - 1:
                return True

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == word[idx + 1]:
                    visited[nx][ny] = True
                    if dfs(nx, ny, idx + 1):
                        return True
                    visited[nx][ny] = False

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[target]:
                    visited[i][j] = True
                    if dfs(i, j, 0):
                        return True
                    visited[i][j] = False

        return False
