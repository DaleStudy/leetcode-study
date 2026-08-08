"""
Time Complexity: O(m * n)
Space Complexity: O(m * n)

Dynamic Programming (2D DP approach):
- Use a 2D array where maze[i][j] represents the number of unique paths to cell (i, j).
- Initialize the first row and first column with 1 (since there's only one way to reach each cell: only right moves for the first row or only down moves for the first column).
- For all other cells, maze[i][j] = maze[i-1][j] + maze[i][j-1] (sum of paths from the cell above and the cell to the left).
- Return maze[m-1][n-1] as the answer, which is the total number of unique paths.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        maze = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                maze[i][j] = maze[i - 1][j] + maze[i][j - 1]

        return maze[m - 1][n - 1]

"""
Time Complexity: O(m * n)
Space Complexity: O(n)

Dynamic Programming (1D DP optimization):
- Use a 1D array dp of size n.
- dp[c] keeps track of the number of unique paths to column c in the current row.
- Initialize dp with 1s (the first row has only one way to reach each column).
- For every row from the second onward, update dp[c] = dp[c] + dp[c - 1] (add ways from the left neighbor to ways accumulated so far).
- Return dp[-1] as the answer, representing the number of unique paths to the bottom-right cell.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(m - 1):
            for c in range(1, n):
                dp[c] += dp[c - 1]

        return dp[-1]

"""
Time Complexity: O(m + n)
Space Complexity: O(1)

Combinatorial approach:
- The problem reduces to choosing (m-1) moves down from (m+n-2) total movements (or equivalently (n-1) moves right).
- The number of unique paths is given by the formula (m+n-2)! / [(m-1)! * (n-1)!], representing all possible orderings of down and right moves.
- Use the combinatorial (factorial) formula to compute the result efficiently.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)

"""
Time Complexity: O(m * n)
Space Complexity: O(m * n)

### Top down dynamic programming (with memoization) ###

Approach:
- Use recursion with memoization (via functools.cache) to store the number of unique paths to (row, col).
- The recursive function dp(row, col) returns the number of unique paths from the top-left to (row, col).
- Base case: If row == 1 or col == 1, there's only one unique path.
- Otherwise, dp(row, col) = dp(row-1, col) + dp(row, col-1).
- The answer is dp(m, n), the number of unique paths to the bottom-right cell.
"""
class Solution:
    @cache
    def uniquePaths(self, m: int, n: int) -> int:
        return 1 if (m == 1 or n == 1) else self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
