from typing import List

class Solution:
    """
        - Time Complexity: O(N), N = The number of items = len(grid) * len(grid[0])
        - Space Complexity: O(N)
            - In worst case (all "1"s), The depth of dfs is N => O(N)
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return
            
            grid[i][j] = "#"    # Visited
            for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                dfs(i + dx, j + dy)               

        count = 0            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        
        return count

tc = [
        ([
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ], 1),
        ([
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ], 3)
]

sol = Solution()
for i, (grid, e) in enumerate(tc, 1):
    r = sol.numIslands(grid)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
