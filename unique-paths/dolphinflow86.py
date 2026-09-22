# M is the number of rows, and N is the number of columns.
# TC: O(M * N) - calculates the number of paths from each cell once
# SC: O(M * N) - uses a memo dictionary and the recursion stack
class Solution:

    def dfs(self, row, col, m, n, memo):
        if row == m - 1 and col == n - 1:
            return 1

        if row >= m or col >= n:
            return 0

        if (row, col) in memo:
            return memo[(row, col)]

        memo[(row, col)] = (
            self.dfs(row + 1, col, m, n, memo)
            + self.dfs(row, col + 1, m, n, memo)
        )
        return memo[(row, col)]

    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        return self.dfs(0, 0, m, n, memo)
