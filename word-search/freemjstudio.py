class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        answer = False

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for _ in range(n)]

        def dfs(x, y, visited, route):
            nonlocal answer
            if route == word:
                answer = True
                return
            if (len(route) == len(word)) and route != word:
                return

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    idx = len(route)
                    if word[idx] == board[nx][ny]:
                        visited[nx][ny] = True
                        route += board[nx][ny]
                        dfs(nx, ny, visited, route)
                        visited[nx][ny] = False
                        route = route[:-1]

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    dfs(i, j, visited, word[0])
                    visited[i][j] = False

        return answer
