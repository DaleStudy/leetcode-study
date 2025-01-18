class Solution:
    # O(m*n), m = len(row), n = len(column)
    def spiralOrder(self, m: list[list[int]]) -> list[int]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        visited = set()
        heading, count = 0, 0
        r, c = 0, 0
        while count < len(m) * len(m[0]):
            result.append(m[r][c])
            visited.add((r, c))
            count += 1
            next_r, next_c = r + dirs[heading][0], c + dirs[heading][1]
            if not (0 <= next_r < len(m) and 0 <= next_c < len(m[0])) or (next_r, next_c) in visited:
                heading = (heading + 1) % 4
                next_r, next_c = r + dirs[heading][0], c + dirs[heading][1]
            r, c = next_r, next_c
        return result
