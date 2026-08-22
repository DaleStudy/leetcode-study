class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_set = set()
        atlantic_set = set()

        m = len(heights)
        n = len(heights[0])

        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(start: tuple[int], row: int, col: int, prev_water: int, prev: set[int]):
            if (row, col) in prev:
                return

            prev.add((row, col))

            if prev_water < heights[row][col]:
                return

            if row == 0 or col == 0:
                pacific_set.add(start)

            if row == m - 1 or col == n - 1:
                atlantic_set.add(start)

            for dr, dc in DIR:
                next_r, next_c = row + dr, col + dc
                if 0 <= next_r < m and 0 <= next_c < n and heights[row][col] >= heights[next_r][next_c]:
                    dfs(start, next_r, next_c, heights[row][col], prev)


        for row in range(m):
            for col in range(n):
                prev = set()
                dfs((row, col), row, col, 10000000, prev)

        res = []
        for row in range(m):
            for col in range(n):
                if (row, col) in pacific_set and (row, col) in atlantic_set:
                    res.append((row, col))

        return res
