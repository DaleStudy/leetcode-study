"""
Time Complexity: O(m * n)
Space Complexity: O(m * n)

### BFS Approach ###

Approach:
- Use BFS to traverse all parts of each island in the grid.
- Employ a queue to process all adjacent land cells iteratively.
- Use a 'bound' helper function to check if a cell is within the grid bounds.
- In 'island_marker', mark visited '1's with '#' to avoid revisiting.
- For every cell in the grid, when a land cell ('1') is encountered, initiate BFS and increment the island count.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIR = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        ROW = len(grid)
        COL = len(grid[0])

        def bound(row: int, col: int) -> bool:
            return 0 <= row < ROW and 0 <= col < COL

        def island_marker(row: int, col: int) -> None:
            q = deque([(row, col)])
            grid[row][col] = "#"

            while q:
                r, c = q.popleft()

                for dr, dc in DIR:
                    tr, tc = r + dr, c + dc

                    if not bound(tr, tc) or grid[tr][tc] != "1":
                        continue

                    grid[tr][tc] = "#"
                    q.append((tr, tc))

        ans = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    island_marker(r, c)
                    ans += 1

        return ans

"""
Time Complexity: O(m * n)
Space Complexity: O(m * n)

### DFS Approach ###

Approach:
- Use DFS to traverse all parts of each island in the grid.
- Visitation is done recursively rather than with a stack, so stack comment is removed for clarity.
- Use a 'bound' helper function to check if a cell is within the grid bounds.
- In 'island_marker', mark visited '1's with '#' to avoid revisiting.
- For every cell in the grid, when a land cell ('1') is encountered, initiate DFS and increment the island count.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIR = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        ROW = len(grid)
        COL = len(grid[0])

        def bound(row: int, col: int) -> bool:
            return 0 <= row < ROW and 0 <= col < COL

        def island_marker(row: int, col: int) -> None:
            grid[row][col] = '#'

            for dr, dc in DIR:
                tr, tc = row + dr, col + dc
                if bound(tr, tc) and grid[tr][tc] == '1':
                    island_marker(tr, tc)

        ans = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    island_marker(r, c)
                    ans += 1

        return ans
