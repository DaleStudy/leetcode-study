from typing import List
from collections import deque

# time O(mn), saoce O(mn)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        # 방문 배열
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r, c, visited):
            queue = deque([(r, c)])
            visited[r][c] = True

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if (0 <= new_r < m and 0 <= new_c < n
                            and not visited[new_r][new_c]
                            and heights[new_r][new_c] >= heights[r][c]):
                        visited[new_r][new_c] = True
                        queue.append((new_r, new_c))

        for i in range(n):
            bfs(0, i, pacific)
            bfs(m - 1, i, atlantic)
        for i in range(m):
            bfs(i, 0, pacific)
            bfs(i, n - 1, atlantic)

        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])

        return result



