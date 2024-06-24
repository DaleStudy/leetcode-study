# TC : O(n) where n is the number of elements in the two-dimensional list.
# SC : O(n) where n is the depth of the stack of recursive calls.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            # Mark the current cell as visited by setting it to "0"
            grid[r][c] = "0"
            # Explore all four possible directions (right, down, left, up)
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                # Check if the new position is within bounds and is land ("1")
                if (
                    0 <= nr < len(grid)
                    and 0 <= nc < len(grid[0])
                    and grid[nr][nc] == "1"
                ):
                    dfs(nr, nc)

        island_count = 0
        # Traverse each cell in the grid
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":  # Found an island
                    island_count += 1  # Increment the island count
                    dfs(r, c)  # Sink the entire island
        return island_count  # Return the total number of islands
