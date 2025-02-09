# Time Complexity: O(N * M), where N is the number of rows and M is the number of columns.
# Space Complexity: O(N * M), in the worst case if the grid is entirely land.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # get the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])
        
        # define a dfs function to mark visited cells
        def dfs(i, j):
            # if out of bounds or the cell is water, stop here
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0":
                return True
            
            # mark the current cell as visited by changing "1" to "0"
            grid[i][j] = "0"
            
            # visit recursively all neighboring cells
            return True if (dfs(i - 1, j) and dfs(i + 1, j) and dfs(i, j - 1) and dfs(i, j + 1)) else False
        
        count = 0
        # loop through the entire grid to find islands
        for i in range(rows):
            for j in range(cols):
                # if we find land ("1"), start a dfs
                if grid[i][j] == "1":
                    # increment count if dfs confirms a new island
                    if dfs(i, j):
                        count += 1
        return count
