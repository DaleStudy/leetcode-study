'''
# 200. Number of Islands

use DFS to find the number of islands (to find the all the possible cases)

## Time and Space Complexity

```
TC: O(m * n)
SC: O(m * n)
```

### TC is O(m * n):
- dfs function is called for each cell in the grid for checking is the land ("1") = O(m * n)

### SC is O(m * n):
- using a recursive function, the call stack can go as deep as the number of cells in the grid in the worst case. = O(m * n)
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] == "0" :
                return
        
            grid[y][x] = "0"
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
        
        island_count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    dfs(x, y)
                    island_count += 1

        return island_count
