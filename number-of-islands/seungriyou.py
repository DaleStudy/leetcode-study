# https://leetcode.com/problems/number-of-islands/

from typing import List

class Solution:
    def numIslands_bfs(self, grid: List[List[str]]) -> int:
        """
        [Complexity]
            - TC: O(m * n)
            - SC: O(m * n)

        [Approach]
            BFS를 사용한다.
        """
        from collections import deque

        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
        m, n = len(grid), len(grid[0])
        res = 0

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = "0"

            while q:
                r, c = q.popleft()

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    # nr, nc가 (1) 범위 내이면서 (2) 아직 방문하지 않은 곳이라면
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1

        return res

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        [Complexity]
            - TC: O(m * n)
            - SC: O(m * n) (call stack)

        [Approach]
            DFS를 사용한다.
        """
        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            # base condition
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] == "0":
                return

            # visited 처리
            grid[r][c] = "0"

            # recur
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1

        return res
