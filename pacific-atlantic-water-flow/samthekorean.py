# m is number of rows and n is number of columns
# TC : O(m*n)
# SC : O(m*n)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific, atlantic = set(), set()
        result: List[List[int]] = []

        def dfs(
            r: int, c: int, ocean_set: Set[Tuple[int, int]], prev_height: int
        ) -> None:
            if (
                r < 0
                or r >= ROWS
                or c < 0
                or c >= COLS
                or (r, c) in ocean_set
                or heights[r][c] < prev_height
            ):
                return

            ocean_set.add((r, c))

            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc, ocean_set, heights[r][c])

        # Water Flow Simulation from Pacific (Top and Left borders)
        for col in range(COLS):
            dfs(0, col, pacific, heights[0][col])
            dfs(ROWS - 1, col, atlantic, heights[ROWS - 1][col])

        for row in range(ROWS):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, COLS - 1, atlantic, heights[row][COLS - 1])

        # Finding cells reachable by both Pacific and Atlantic
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
