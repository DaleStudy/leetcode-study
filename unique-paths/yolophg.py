# Time Complexity: O(N * M) : iterate through a grid of size m x n once.
# Space Complexity: O(N * M) : use a DP table of size (m+1) x (n+1) to store the number of paths.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create a dp table and add extra rows and columns for easier indexing
        table = [[0 for x in range(n+1)] for y in range(m+1)]
        
        # set the starting point, one way to be at the start
        table[1][1] = 1

        # iterate the grid to calculate paths
        for i in range(1, m+1):
            for j in range(1, n+1):
                # add paths going down
                if i+1 <= m:
                    table[i+1][j] += table[i][j] 
                # add paths going right
                if j+1 <= n:
                    table[i][j+1] += table[i][j]
        
        return table[m][n]
