class Solution:
    # 시간복잡도: O(N*M)
    # 공간복잡도: O(N*M)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        dp = [[False] * (n) for _ in range(m)]
        dp[0][n - 1] = True
        dp[m - 1][0] = True
        visited = set()

        def dfs(x, y):
            if dp[x][y]:
                return 2

            check = set()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) not in visited and heights[nx][ny] <= heights[x][y]:
                        visited.add((nx, ny))
                        res = dfs(nx, ny)

                        if res != -1:
                            check.add(res)
                        visited.remove((nx, ny))
                else:
                    if x == 0 or y == 0:
                        check.add(0)
                    if x == m - 1 or y == n - 1:
                        check.add(1)

            if 2 in check:
                dp[x][y] = 2
                return 2

            if len(check) == 2:
                return 2

            if check:
                return check.pop()

            return -1

        answer = []
        for i in range(m):
            for j in range(n):
                if dfs(i, j) == 2:
                    answer.append([i, j])

        return answer
