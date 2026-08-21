# M is the number of rows, and N is the number of columns.
# TC: O(M * N) - visits each cell constant number of times via DFS
# SC: O(M * N) - stores visited sets and recursion stack for both oceans


class Solution:

    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if (r, c) in visited or heights[r][c] < prev_height:
                return

            visited.add((r, c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        return [[r, c] for r, c in pacific & atlantic]
