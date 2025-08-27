from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dr = (0, 1, 0, -1)
        dc = (1, 0, -1, 0)
        r, c, d = 0, 0, 0

        n, m = len(matrix), len(matrix[0])

        result = []
        VISITED = None
        for _ in range(n * m):
            result.append(matrix[r][c])
            matrix[r][c] = VISITED

            nr, nc = r + dr[d], c + dc[d]

            if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] != VISITED:
                r, c = nr, nc
                continue

            d = (d + 1) % 4
            r += dr[d]
            c += dc[d]

        return result
