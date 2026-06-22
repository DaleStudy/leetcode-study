"""
# Approach
태평양 가장자리에서 출발해서, 물이 거꾸로 올라올 수 있는 칸들을 찾고 대서양도 똑같이 찾은 뒤 둘의 교집합을 구한다.

# Complexity
- Time complexity: O(rows * cols)
- Space complexity: O(rows * cols)
"""

from collections import deque


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(starts):
            visited = set(starts)
            q = deque(starts)

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue
                    if (nr, nc) in visited:
                        continue

                    # 역방향: 현재보다 같거나 높은 곳으로 이동 가능
                    if heights[nr][nc] < heights[r][c]:
                        continue

                    visited.add((nr, nc))
                    q.append((nr, nc))

            return visited

        pacific_starts = []
        atlantic_starts = []

        for r in range(rows):
            pacific_starts.append((r, 0))
            atlantic_starts.append((r, cols - 1))

        for c in range(cols):
            pacific_starts.append((0, c))
            atlantic_starts.append((rows - 1, c))

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return [[r, c] for r, c in pacific & atlantic]
