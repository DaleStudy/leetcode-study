from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # If the input is empty, return an empty list
        if not heights:
            return []

        # Get the number of rows and columns in the grid
        row_length, col_length = len(heights), len(heights[0])

        # Initialize 2D arrays to track cells reachable by Pacific and Atlantic oceans
        pacific_reachable = [
            [False for _ in range(col_length)] for _ in range(row_length)
        ]
        atlantic_reachable = [
            [False for _ in range(col_length)] for _ in range(row_length)
        ]

        # Define a depth-first search (DFS) function
        def dfs(row, col, reachable, prev_height):
            # Terminate if the cell is out of bounds, already visited, or has a lower height
            if (
                row < 0
                or col < 0
                or row >= row_length
                or col >= col_length
                or reachable[row][col]
                or heights[row][col] < prev_height
            ):
                return

            # Mark the current cell as reachable
            reachable[row][col] = True

            # Perform DFS in all four directions
            for delta_row, delta_column in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(row + delta_row, col + delta_column, reachable, heights[row][col])

        # Start DFS from the edges of the grid that are adjacent to the Pacific and Atlantic oceans
        for i in range(row_length):
            dfs(i, 0, pacific_reachable, heights[i][0])  # Pacific side
            dfs(
                i, col_length - 1, atlantic_reachable, heights[i][col_length - 1]
            )  # Atlantic side

        for j in range(col_length):
            dfs(0, j, pacific_reachable, heights[0][j])  # Pacific top
            dfs(
                row_length - 1, j, atlantic_reachable, heights[row_length - 1][j]
            )  # Atlantic bottom

        result = []

        # Collect cells that can reach both the Pacific and Atlantic oceans
        for r in range(row_length):
            for c in range(col_length):
                if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                    result.append([r, c])

        return result
